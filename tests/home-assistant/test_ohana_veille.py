"""The Home Assistant watch package: entities, triggers and alert wording."""

import unittest
from pathlib import Path

import yaml

try:
    import jinja2
except ImportError:  # the wording check needs Home Assistant's template engine
    jinja2 = None

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "config/home-assistant/ohana-veille.yaml"

# Verified on HA-01: the Agent's "Alertes actives" sensor.
ALERTS = "sensor.ohana_platform_alertes_actives"


def load() -> dict:
    return yaml.safe_load(PACKAGE.read_text(encoding="utf-8"))


class VeillePackageTests(unittest.TestCase):
    def setUp(self):
        self.package = load()
        self.automations = {item["id"]: item for item in self.package["automation"]}

    def test_polls_vision_unauthenticated_over_the_lan_by_address(self):
        (resource,) = self.package["rest"]
        # An address, not a name: the watch must not depend on INFRA-01's DNS.
        self.assertEqual(resource["resource"], "http://192.168.1.10:8000/api/runtime/vitals")
        self.assertLessEqual(resource["scan_interval"], 60)
        names = {sensor["unique_id"] for sensor in resource["binary_sensor"]}
        self.assertEqual(names, {"ohana_veille_vision", "ohana_veille_agent"})

    def test_alert_triggers_cover_mute_vision_agent_and_active_alerts(self):
        triggers = self.automations["ohana_veille_alerte"]["triggers"]
        watched = {
            entity
            for trigger in triggers
            for entity in (
                trigger["entity_id"]
                if isinstance(trigger["entity_id"], list)
                else [trigger["entity_id"]]
            )
        }
        self.assertEqual(
            watched,
            {
                "binary_sensor.ohana_veille_vision",
                "binary_sensor.ohana_veille_agent",
                ALERTS,
            },
        )
        # A short blip never wakes the phone.
        for trigger in triggers:
            self.assertIn("for", trigger)
        stuck = triggers[0]
        self.assertEqual(stuck["to"], ["off", "unavailable"])

    def test_notification_is_replaced_not_stacked_and_cleared_on_recovery(self):
        alert = self.automations["ohana_veille_alerte"]["actions"][-1]
        recovery = self.automations["ohana_veille_retablie"]["actions"][-1]
        self.assertEqual(alert["data"]["data"]["tag"], "ohana-veille")
        self.assertEqual(recovery["data"]["message"], "clear_notification")
        self.assertEqual(recovery["data"]["data"]["tag"], "ohana-veille")
        # The owner must pick their phone: the placeholder is explicit.
        self.assertEqual(alert["action"], "notify.mobile_app_REMPLACER")
        self.assertEqual(recovery["action"], "notify.mobile_app_REMPLACER")

    @unittest.skipIf(jinja2 is None, "jinja2 is required to render the alert wording")
    def test_alert_wording_for_each_failure(self):
        template = self.automations["ohana_veille_alerte"]["actions"][0]["variables"]["problems"]

        def render(states: dict[str, str]) -> str:
            environment = jinja2.Environment()
            environment.filters["int"] = lambda value, default=0: (
                int(value) if str(value).lstrip("-").isdigit() else default
            )
            return (
                environment.from_string(template)
                .render(
                    is_state=lambda entity, value: states.get(entity) == value,
                    states=lambda entity: states.get(entity, "unknown"),
                )
                .strip()
            )

        vision = "binary_sensor.ohana_veille_vision"
        agent = "binary_sensor.ohana_veille_agent"
        healthy = {vision: "on", agent: "on", ALERTS: "0"}
        self.assertEqual(render(healthy), "")
        self.assertEqual(
            render({**healthy, vision: "unavailable", agent: "unavailable"}),
            "Vision ou INFRA-01 ne répondent pas",
        )
        self.assertEqual(
            render({**healthy, agent: "off"}),
            "L'Agent ne livre plus ses observations",
        )
        self.assertEqual(
            render({**healthy, ALERTS: "3"}),
            "3 alerte(s) active(s)",
        )
        self.assertEqual(
            render({**healthy, ALERTS: "unavailable"}),
            "L'Agent ne publie plus son état",
        )
        self.assertEqual(
            render({**healthy, agent: "off", ALERTS: "2"}),
            "L'Agent ne livre plus ses observations ; 2 alerte(s) active(s)",
        )


if __name__ == "__main__":
    unittest.main()
