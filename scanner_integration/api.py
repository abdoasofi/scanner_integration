import frappe
from frappe import _
import requests
import os
from tempfile import NamedTemporaryFile

def fetch_and_attach_files(doctype, docname):

    try:
        # Simulate fetching files from a printer (replace with your actual printer logic)
        files = simulate_fetch_files_from_printer()

        if not files:
            return {"success": False, "error":_("No files found from scanner.")}


        for filename, filecontent in files.items():
            # Create a temporary file
            with NamedTemporaryFile(delete=False) as tmpfile:
                tmpfile.write(filecontent)
                tmp_file_path = tmpfile.name

            # Attach the file to the document using Frappe API
            try:
                attached_file = frappe.attach_file(
                    filename=filename,
                    file_path=tmp_file_path,
                    doctype=doctype,
                    docname=docname
                )

            finally: #always delete the temp file even if attachement fails
               os.remove(tmp_file_path)

            if not attached_file:
                 return {"success": False, "error":_("Could not attach the file.")}

        return {"success": True}

    except Exception as e:
         return {"success": False, "error": str(e)}


def simulate_fetch_files_from_printer():
    # This is a simulated example. Replace with your logic to interact with your printer.
    # Ideally this would involve calling the printer's API.
    # For this simulation, we are generating sample file data
   pass