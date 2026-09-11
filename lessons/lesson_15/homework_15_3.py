from core.config import PROJECT_DIR
from core.utils.logger import cli_logger
import xml.etree.ElementTree as ET

test_dir = PROJECT_DIR / "lessons" / "lesson_15"
xml_file = test_dir / "groups.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

def get_incoming_by_group_number(group_number):
    groups = root.findall("group")

    for group in groups:
        number = group.find("number")
        if number.text == group_number:
            timing_exbytes = group.find("timingExbytes")
            incoming = timing_exbytes.find("incoming")
            return incoming.text
    return None

cli_logger.info(get_incoming_by_group_number("2"))

