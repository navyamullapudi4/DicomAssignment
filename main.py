# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pydicom

def list_tags(ds, tagname=""):
    return ds.dir(tagname)

def modify_tag(ds, tagname, tagvalue, outputfilename):
    de = ds[tagname]
    de.value = tagvalue
    ds.save_as(outputfilename)

def delete_tag(ds, tagname, outputfilename):
    del ds[tagname]
    ds.save_as(outputfilename)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     filename="data/693_J2KR.dcm"
#     outputfilename = "data/693_J2KR_modified.dcm"
#
#     ds = pydicom.dcmread(filename)
#     print(list_tags(ds))
#
#     modify_tag(ds, "PatientName","john",outputfilename)
#     delete_tag(ds, "Columns", outputfilename)


import unittest

class TestMethods(unittest.TestCase):

    def setUp(self):
        self.filename = "data/693_J2KR.dcm"
        self.ds = pydicom.dcmread(self.filename)
        self.tagname = "PatientName"
        self.outputfilename = "data/693_J2KR_modified.dcm"

    def test_list_tags(self):
        actual = ["PatientName"]
        expected = list_tags(self.ds, self.tagname)
        self.assertEqual(actual, expected)

    def test_modify_tag(self):
        tagvalue = "sodhigaada"
        modify_tag(self.ds, self.tagname, tagvalue, self.outputfilename)
        output_data = pydicom.dcmread(self.outputfilename)
        expected = output_data[self.tagname].value
        actual = tagvalue
        self.assertEqual(actual, expected)

    def test_delete_tag(self):
        delete_tag(self.ds, self.tagname, self.outputfilename)
        output_data = pydicom.dcmread(self.outputfilename)
        self.assertFalse(self.tagname in output_data)