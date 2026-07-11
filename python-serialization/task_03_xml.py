#!/usr/bin/env python3
"""Module for serializing and deserializing data using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    """Serialize a dictionary to XML and save it to filename.

    Args:
        data (dict): The data to serialize.
        filename (str): The output XML file.
    """
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Parse an XML file and reconstruct it as a dictionary.

    Args:
        filename (str): The input XML file.

    Returns:
        dict: The reconstructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
