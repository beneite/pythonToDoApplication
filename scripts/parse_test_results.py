# scripts/parse_test_results.py
import xml.etree.ElementTree as ET

tree = ET.parse("report.xml")
root = tree.getroot()

total = int(root.attrib.get("tests", 0))
failures = int(root.attrib.get("failures", 0))
errors = int(root.attrib.get("errors", 0))
skipped = int(root.attrib.get("skipped", 0))
passed = total - failures - errors - skipped

summary = (
    f"🧪 *Test Report by Ashish*:\n"
    f"✅ Passed: {passed}\n"
    f"❌ Failed: {failures + errors}\n"
    f"⚠️ Skipped: {skipped}\n"
    f"📊 Total: {total}"
)

with open("slack_msg.txt", "w") as f:
    f.write(summary)
