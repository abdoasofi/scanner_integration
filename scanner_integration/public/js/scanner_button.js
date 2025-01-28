frappe.ui.form.on('Form', {  
    // Listen to 'Form' instead of specific doctype to apply to all forms

    refresh: function(frm) {

        if (!frm.is_new()) { 
            // Don't add button on new form
            frm.add_custom_button(__('Attach from Scanner'), () => {
                
                frappe.call({
                    method: "scanner_integration.api.fetch_and_attach_files", // Server-side API endpoint
                    args: {
                        doctype: frm.doc.doctype,
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message && r.message.success) {
                            frappe.show_alert({
                                message: __('Files attached successfully!'),
                                indicator: 'green'
                            });
                             frm.reload_doc(); // Reload the form to display newly attached files
                        } else if(r.message && r.message.error) {
                          frappe.show_alert({
                                message: __('Error attaching files: ') + r.message.error,
                                indicator: 'red'
                            });

                        } else{
                          frappe.show_alert({
                                message: __('Error attaching files: Unknown error'),
                                indicator: 'red'
                            });
                        }
                    }
                });
            });
        }
    }
});