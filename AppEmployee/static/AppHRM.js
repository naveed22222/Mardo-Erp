AppHRMModel = function () {

    var me = this;
    me.selItemCount = 1;
    me.Employee_OBJ = [];
    me.appConstructor = function () {
    }

    ////DISPLAY BOX FOR ADDED EMPLOYEE position
    me.ShowBox_AddEmployeeDepartment = function (param) {
        // alert(param);

        var split = param.split(",");

        var action_type = split[0];
        var department_id = "";
        var department_name = "";
        if (action_type === "UPDATE") {
            department_id = split[1];
            department_name = split[2];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_department"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='department_id' name='department_id' value='" + department_id + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Department Name: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="department_name" name="department_name" ' + "placeholder='e.g. Accounting, Human Resource, Outlet' value='" + department_name + "'></div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddEmployeeDepartment();" class="btn btn-sm w-50 btn-success" type="button">Save Department</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_emp_department").html("Add new employee department");
        if (split[0] === "UPDATE") {
            $("#department_name").val(split[2]);
            $("#title_emp_department").html("update employee department");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    ////ADDED NEW EMPLOYEE DEPARTMENT
    me.AddEmployeeDepartment = function () {
        var action_type = $("#action_type").val();
        var department_id = $("#department_id").val();
        var department_name = $("#department_name").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('department_id', department_id);
        formdata.append('department_name', department_name);

        swal({
            title: "Employee Department",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_emp_department,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.message);
                    if (data.message === "Success") {
                        location.reload();
                    }
                });
            } else {
                swal("Cancelled", "Please Re-check your Status :)", "error");
            }
        });

    }

    ////DELETED EMPLOYEE DEPARTMENT
    me.DeleteEmployeeDepartmentView = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this !",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {
                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_emp_department,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.PV_List);
                    swal("Deleted!", "Your Department has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Department is safe :)", "error");
            }
        });
    }

    ////DISPLAY BOX FOR ADDED EMPLOYEE POSITION
    me.ShowBox_AddEmployeePosition = function (param) {
        var split = param.split(",");

        var action_type = split[0];
        var position_id = "";
        var position_name = "";
        if (action_type === "UPDATE") {
            position_id = split[1];
            position_name = split[2];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_position"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='position_id' name='position_id' value='" + position_id + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Position Name: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="position_name" name="position_name" ' + "placeholder='e.g. Manager, Cook, Waiter, Delivery, Office Boy' value='" + position_name + "'></div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddEmployeePosition();" class="btn btn-sm w-50 btn-success" type="button">Save Position</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_emp_position").html("Add new employee position");
        if (split[0] === "UPDATE") {
            $("#position_name").val(split[2]);
            $("#title_emp_position").html("update employee position");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    ////ADDED NEW EMPLOYEE POSITION
    me.AddEmployeePosition = function () {
        var action_type = $("#action_type").val();
        var position_id = $("#position_id").val();
        var position_name = $("#position_name").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('position_id', position_id);
        formdata.append('position_name', position_name);

        swal({
            title: "Employee Position",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_emp_position,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.message);
                    if (data.message === "Success") {
                        location.reload();
                    }
                });
            } else {
                swal("Cancelled", "Please Re-check your Status :)", "error");
            }
        });
    }

    ////DELETED EMPLOYEE POSITION
    me.DeleteDepartmentPositionView = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this !",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_emp_position,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.PV_List);
                    swal("Deleted!", "Your Position has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Position is safe :)", "error");
            }
        });
    }

    //// SINGLE EMPLOYEE PAYMENT METHOD (START)
    me.ShowBox_AddEmployeePayment = function (param) {
        var split = param.split(',');
        var action_type = split[0];
        var hidden_emp_code = "";
        var employee_payment_id = "";
        var payment_method = "";
        var bank_name = "";
        var account_title = "";
        var account_number = "";

        if (action_type === "UPDATE") {
            employee_payment_id = split[1]
            payment_method = split[2];
            bank_name = split[3];
            account_title = split[4];
            account_number = split[5];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_pay"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='hidden_emp_code' name='hidden_emp_code' value='" + hidden_emp_code + "' autocomplete='off'>" + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='employee_payment_id' name='employee_payment_id' value='" + employee_payment_id + "' autocomplete='off'>" +

            '<label for="recipient-name" class="col-form-label">Payment Type: <small class="text-warning">*</small></label>' + '<select id="cmd_payment_method_id" name="cmd_payment_method_id" class="form-control text-capitalize">' + '<option value="NA">Select Payment Type</option>' + '</select>' + '<div id="bank_name_condition" style="display: none;">' + '<label for="recipient-name" class="col-form-label">Bank Name: <small class="text-warning">*</small></label>' + '<select id="cmd_bank_name_id" name="cmd_bank_name_id" class="form-control form-select select2-no-search text-capitalize">' + '<option value="NA">Select Bank Name</option>' + '</select>' + '</div>' + '<div id="account_title_condition" style="display: block;">' + '<label for="recipient-name" class="col-form-label">Account Title: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="account_title" name="account_title" ' + "placeholder='e.g. Enter Account Title' value='" + account_title + "'>" + '</div>' + '<div id="account_number_condition" style="display: block;">' + '<label for="recipient-name" class="col-form-label">Account No: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="account_number" name="account_number" ' + "placeholder='e.g. enter account number' value='" + account_number + "'>" + '</div>' + "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddEmployeePayment();" class="btn btn-sm w-50 btn-success" type="button">Save Category</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        // var get_payment_name = "";
        $("#cmd_payment_method_id").change(function (e) {
            // get_payment_name = e.target.value;

            var get_payment_name = $("#cmd_payment_method_id :selected ").text().toLowerCase();
            // alert(get_payment_name);

            if (get_payment_name === "bank") {

                $("#bank_name_condition").css("display", "block");
            } else {
                $("#bank_name_condition").css("display", "none");
            }

        });

        $("#title_emp_pay").html("Add new payment");
        if (split[0] === "UPDATE") {
            $("#title_emp_pay").html("update employee payment name");
        }

        $("#cmd_payment_method_id").select2();
        HRMModelJS.FillCmdPaymentMethod_EMP("cmd_payment_method_id", payment_method);

        $("#cmd_bank_name_id").select2();
        GlobalModelJS.FillCmdListByModel("tbl_bank_data", "bank_name", "bank_code", "cmd_bank_name_id", bank_name);

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }


    // ADDED NEW EMPLOYEE PAYMENT
    me.AddEmployeePayment = function () {
        var hidden_emp_code = $("#hidden_emp_code").val();
        var action_type = $("#action_type").val();
        var employee_payment_id = $("#employee_payment_id").val();
        var cmd_payment_method_id = $("#cmd_payment_method_id").val();
        var cmd_bank_name_id = $("#cmd_bank_name_id").val();
        var account_title = $("#account_title").val();
        var account_number = $("#account_number").val();
        let formdata = new FormData();

        formdata.append('hidden_emp_code', hidden_emp_code);
        formdata.append('action_type', action_type);
        formdata.append('employee_payment_id', employee_payment_id);
        formdata.append('cmd_payment_method_id', cmd_payment_method_id);
        formdata.append('cmd_bank_name_id', cmd_bank_name_id);
        formdata.append('account_title', account_title);
        formdata.append('account_number', account_number);

        swal({
            title: "Employee Payment",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_emp_payment,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    $("#emp_pay_body").empty("");
                    let pay = data.payment_list;
                    var loopCount = 1;
                    for (let i = 0; i < pay.length; i++) {
                        let editParam = "UPDATE," + data.payment_list[i].id + "," + data.payment_list[i].pm_code_id + "^^" + data.payment_list[i].pm_name + "," + data.payment_list[i].bank_code_id + "," + data.payment_list[i].account_title + "," + data.payment_list[i].account_number;
                        let deleteParam = data.payment_list[i].payment_code;
                        $("#emp_pay_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + loopCount + '</td>' + '<td id="payment_name"' + loopCount + ' class="xsm-text text-capitalize align-middle text-center">' + data.payment_list[i].pm_name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.payment_list[i].bank_code_id + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.payment_list[i].account_number + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.payment_list[i].account_title + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.payment_list[i].status + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_AddEmployeePayment('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.DeleteEmployeePayment('" + deleteParam + "');>" + '<i class="fe fe-trash"></i>' + '</button>' + '</td>' + '</tr>');

                        if (data.payment_list[i].pm_name === "Cash") {
                            $("#payment_name" + loopCount).val("-")
                        }

                        loopCount++;
                    }
                    swal.close();
                    $('#effectModal').modal('hide');
                });
            }
        });
    }


    me.DeleteEmployeePayment = function (code) {
        GlobalModelJS.DeleteData('tbl_employee_payment_method', 'payment_code', code, HRMModelJS.ShowBox_AddEmpPayMethodWithoutRefresh);
    }

    // CONDITION ON ADD EMPLOYEE PAYMENT
    me.FillCmdPaymentMethod_EMP = function (cmd_id, selected_value) {
        var paramas = {
            url: cmd_payment_method, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.cmd_list.length; i++) {
                if (data.cmd_list[i]["pm_code"] !== "PM-1") {
                    sbox.add(new Option(data.cmd_list[i]["pm_name"], data.cmd_list[i]["pm_code"] + "^^" + data.cmd_list[i]["pm_name"]));
                }
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }

        });
    }

    //// SINGLE EMPLOYEE PAYMENT METHOD (END)


    // me.onChangePaymentMethod_EMPINFO = function () {
    //
    //     $("#bank_name_condition").css("display", "block");
    //     $("#account_title_condition").css("display", "block");
    //     $("#account_number_condition").css("display", "block");
    //
    //     // var get_payment_method_code = $("#cmd_payment_method").text();
    //     var get_payment_method_code = $('#cmd_payment_method :selected').text();
    //     // alert(get_payment_method_code);
    //
    //     // if (get_payment_method_code === "PM-1") {
    //     //     $("#bank_name_condition").css("display", "none");
    //     //     $("#cmd_bank_name_id").val("NA");
    //     //     $("#account_title_condition").css("display", "none");
    //     //     $("#account_title").val("NA");
    //     //     $("#account_number_condition").css("display", "none");
    //     //     $("#account_number").val("0");
    //     // }
    //     // if (get_payment_method_code === "PM-3" || get_payment_method_code === "PM-4") {
    //     //     $("#bank_name_condition").css("display", "none");
    //     //     $("#cmd_bank_name_id").val("NA");
    //     // }
    //
    // }

    // me.AddSingleEmployeePaymentMethod = function () {
    //     var hidden_emp_code = $("#hidden_emp_code").val();
    //     var action_type = $("#action_type").val();
    //     var emp_payment_method = $("#inp_emp_payment_method").val();
    //     var cmd_payment_method = $("#cmd_payment_method").val();
    //     var cmd_bank_code = $("#cmd_bank_list").val();
    //     var account_title = $("#account_title").val();
    //     var account_number = $("#account_number").val();
    //     let formdata = new FormData();
    //
    //     formdata.append('hidden_emp_code', hidden_emp_code);
    //     formdata.append('action_type', action_type);
    //     formdata.append('emp_payment_method', emp_payment_method);
    //     formdata.append('cmd_payment_method', cmd_payment_method);
    //     formdata.append('cmd_bank_code', cmd_bank_code);
    //     formdata.append('account_title', account_title);
    //     formdata.append('account_number', account_number);
    //
    //     swal({
    //             title: "Employee Payment",
    //             text: action_type,
    //             type: "success",
    //             showCancelButton: true,
    //             confirmButtonClass: "btn btn-danger",
    //             confirmButtonText: "Yes, Confirm!",
    //             closeOnConfirm: false
    //         },
    //         function (isConfirm) {
    //             if (isConfirm) {
    //                 var paramas = {
    //                     url: add_emp_payment,
    //                     data: formdata,
    //                     type: "POST",
    //                     dataType: 'json',
    //                     headers: {'X-CSRFToken': posttoken}
    //                 };
    //                 callAJAX(paramas, function (data) {
    //
    //                     $("#emp_pay_body").empty("");
    //
    //                     // console.log(data.payment_list.length);
    //                     var loopCount = 1;
    //                     for (let i = 0; i < data.payment_list.length; i++) {
    //                         $("#emp_pay_body").append('<tr>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' + loopCount + '</td>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' + data.payment_list[i].pm_name + '</td>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' + data.payment_list[i].bank_code_id + '</td>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' + data.payment_list[i].account_number + '</td>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' + data.payment_list[i].account_title + '</td>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' + data.payment_list[i].status + '</td>' +
    //                             '<td class="xsm-text text-capitalize align-middle text-left">' +
    //                             '<button class="btn btn-sm btn-def tx-muted" onclick="HRMModelJS.ShowBox_AddEmployeePayment(\'UPDATE\+\data.payment_list[i].pm_name \');"><i class="fe fe-edit"></i></button>' +
    //                             '<button class="btn btn-sm btn-def tx-muted" onclick="HRMModelJS.ShowBox_AddEmployeePayment();"><i class="fe fe-trash"></i></i></button>' +
    //                             '</td>' +
    //                             '</tr>');
    //                         loopCount++;
    //                     }
    //
    //                     swal.close();
    //                     $('#effectModal').modal('hide');
    //
    //                 });
    //             }
    //         });
    // }
    //
    // me.DeleteEmployeePayment = function (id) {
    //     swal({
    //             title: "Are you sure?",
    //             text: "You will not be able to recover this !",
    //             type: "warning",
    //             showCancelButton: true,
    //             confirmButtonClass: "btn-danger",
    //             confirmButtonText: "Yes, Delete it!",
    //             cancelButtonText: "No, Cancel!",
    //             closeOnConfirm: false,
    //             closeOnCancel: false
    //
    //         },
    //         function (isConfirm) {
    //             if (isConfirm) {
    //
    //                 let formdata = new FormData();
    //                 formdata.append('id', id);
    //                 var paramas = {
    //                     url: delete_emp_payment,
    //                     data: formdata,
    //                     type: "POST",
    //                     dataType: 'json',
    //                     headers: {'X-CSRFToken': posttoken}
    //                 };
    //                 callAJAX(paramas, function (data) {
    //                         // console.log(data.PV_List);
    //                         swal("Deleted!", "Your Payment has been deleted.", "success");
    //                         if (data.message === "Success") {
    //                             location.reload();
    //                         }
    //                     }
    //                 );
    //
    //             } else {
    //                 swal("Cancelled", "Your Payment is safe :)", "error");
    //             }
    //         });
    // }

    //// DEDUCTION FUNCTION START
    me.ShowBox_AddDeductionCategory = function (param) {
        // alert(param);
        var split = param.split(',');
        var action_type = split[0];
        var ded_type_code = "";
        var ded_type_name = "";
        var ded_type = "";

        if (action_type === "UPDATE") {
            ded_type_code = split[1];
            ded_type_name = split[2];
            ded_type = split[3];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_category"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='ded_type_code' name='ded_type_code' value='" + ded_type_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Deduction Type<small class="text-warning">*</small></label>' + // '<br>' +
            '<select name="ded_type" id="ded_type" class="form-control">' + '<option value="NA">Select</option>' + '<option value="fixed">Fixed</option>' + '<option value="non-fixed">Non-Fixed</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Deduction Category: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="ded_type_name" name="ded_type_name" ' + "placeholder='Enter Deduction Category' value='" + ded_type_name + "'></div>");


        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddDeductionCategory();" class="btn btn-sm w-50 btn-success" type="button">Save Category</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_emp_category").html("add new category");
        if (split[0] === "UPDATE") {
            $("#ded_type_name").val(split[2]);
            $("#ded_type").val(split[3]);
            $("#title_emp_category").html("update deduction category");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.AddDeductionCategory = function () {
        var action_type = $("#action_type").val();
        var ded_type_code = $("#ded_type_code").val();
        var ded_type = $("#ded_type").val();
        var ded_type_name = $("#ded_type_name").val();

        let formdata = new FormData();

        formdata.append('action_type', action_type);
        formdata.append('ded_type_code', ded_type_code);
        formdata.append('ded_type', ded_type);
        formdata.append('ded_type_name', ded_type_name);

        swal({
            title: "Deduction Category",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_ded_category,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.message);
                    if (data.message === "Success") {
                        location.reload();
                    }
                });
            } else {
                swal("Cancelled", "Please Re-check your Status :)", "error");
            }
        });
    }

    me.DeleteDeductionCategoryView = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this !",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_deduction_category,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    swal("Deleted!", "Your Category has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Category is safe :)", "error");
            }
        });
    }

    // Deduction Fixed Delete Function
    me.DeleteDeductionFixedView = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_deduction_fixed,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    swal("Deleted!", "Your Deduction Fixed has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Deduction Fixed is safe :)", "error");
            }
        });
    }

    //// NON-FIXED DEDUCTION ONLY SELECTED EMPLOYEE PAYMENT METHOD
    me.FillCMDEmpPayMethodOnDedNonFix = function (cmd_id, employee_code, selected_value) {
        let formdata = new FormData();
        formdata.append('cmd_employee', employee_code);
        var paramas = {
            url: PaymentMethodChangeOnEmp,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            $('#' + cmd_id).empty("");
            $('#' + cmd_id).append("<option val=''>Select</option>");
            $("#" + cmd_id + "> option").removeAttr("selected");
            $("#" + cmd_id).trigger("change");

            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.emp_pay_method_list.length; i++) {
                if (data.emp_pay_method_list[i]["pm_name"] === "Cash") {
                    sbox.add(new Option(data.emp_pay_method_list[i]["pm_name"], data.emp_pay_method_list[i]["emp_pm_code"]));
                } else {
                    sbox.add(new Option(data.emp_pay_method_list[i]["pm_name"] + ", " + data.emp_pay_method_list[i]["bank_name"], data.emp_pay_method_list[i]["emp_pm_code"]));
                }
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }
        });
    }

    //// DEDUCTION FUNCTION END

    //// ALLOWANCE FUNCTION START
    me.ShowBox_AddAllowanceCategory = function (param) {
        var split = param.split(',');
        var action_type = split[0];
        var all_type_id = "";
        var all_type = "";
        var all_type_name = "";

        if (action_type === "UPDATE") {
            all_type_id = split[1];
            all_type = split[2];
            all_type_name = split[3];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_allowance_category"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='all_type_id' name='all_type_id' value='" + all_type_id + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Allowance Type: <small class="text-warning">*</small></label>' + '<select name="all_type" id="all_type" class="form-control" data-live-search="True">' + '<option value="NA">Select</option>' + '<option value="fixed">Fixed</option>' + '<option value="non-fixed">Non-Fixed</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Allowance Category: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="all_type_name" name="all_type_name" ' + "placeholder='Enter Allowance Category' value='" + all_type_name + "'></div>");


        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddAllowanceCategory();" class="btn btn-sm w-50 btn-success" type="button">Save Category</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_allowance_category").html("add new category");
        if (split[0] === "UPDATE") {
            $("#all_type").val(split[2]);
            $("#all_type_name").val(split[3]);
            $("#title_allowance_category").html("update allowance category");

        }

        $('#all_type').select2({
            dropdownParent: $('#effectModal')
        });

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.AddAllowanceCategory = function () {
        var action_type = $("#action_type").val();
        var all_type_id = $("#all_type_id").val();
        var all_type = $("#all_type").val();
        var all_type_name = $("#all_type_name").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('all_type_id', all_type_id);
        formdata.append('all_type', all_type);
        formdata.append('all_type_name', all_type_name);

        var paramas = {
            url: add_allowance_category,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            if (data.message === "Success") {
                location.reload();
            }
        });
    }

    me.DeleteAllowanceCategory = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this category!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_allowance_category,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    swal("Deleted!", "Your Category has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Category is safe :)", "error");
            }
        });
    }

    // Allowance Fixed Delete Function
    me.DeleteAllowanceFixed = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_allowance_fixed,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    swal("Deleted!", "Your Allowance Fixed has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Allowance Fixed is safe :)", "error");
            }
        });
    }

    //// ALLOWANCE FUNCTION END


    //// LEAVE FUNCTION START
    me.ShowBox_AddEmployeeHoliday = function (param) {
        var split = param.split("::");

        var action_type = split[0];
        var holiday_id = "";
        var holiday_name = "";
        var holiday_date = "";
        var holiday_description = "";
        if (action_type === "UPDATE") {
            holiday_id = split[1];
            holiday_name = split[2];
            holiday_date = split[3];
            holiday_description = split[4];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_holiday"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='holiday_id' name='holiday_id' value='" + holiday_id + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Holiday Name: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="holiday_name" name="holiday_name" ' + "placeholder='Enter Holiday Name' value='" + holiday_name + "'>" + '<label for="recipient-name" class="col-form-label">Holiday Date: <small class="text-warning">*</small></label>' + '<input class="form-control flatpickr-input active"  name="holiday_date" id="holiday_date" type="text" readonly="readonly" placeholder="Enter a Valid Date" value="' + holiday_date + '">' + '<label for="recipient-name" class="col-form-label">Holiday Description: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="holiday_description" name="holiday_description" ' + "placeholder='Enter Holiday Description' value='" + holiday_description + "'>" + "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddEmployeeHoliday();" class="btn btn-sm w-50 btn-success" type="button">Save Holiday</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_emp_holiday").html("Add new Holiday");
        if (split[0] === "UPDATE") {
            $("#holiday_name").val(split[2]);
            $("#holiday_date").val(split[3]);
            $("#holiday_description").val(split[4]);
            $("#title_emp_holiday").html("update Holiday");
        }

        flatpickr("#holiday_date", {});

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }


    //ADDED NEW EMPLOYEE Holiday
    me.AddEmployeeHoliday = function () {
        var action_type = $("#action_type").val();
        var holiday_id = $("#holiday_id").val();
        var holiday_name = $("#holiday_name").val();
        var holiday_date = $("#holiday_date").val();
        var holiday_description = $("#holiday_description").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('holiday_id', holiday_id);
        formdata.append('holiday_name', holiday_name);
        formdata.append('holiday_date', holiday_date);
        formdata.append('holiday_description', holiday_description);

        swal({
            title: "Employee Holiday",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_national_holiday,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.message);
                    if (data.message === "Success") {
                        location.reload();
                    }
                });
            } else {
                swal("Cancelled", "Please Re-check your Status :)", "error");
            }
        });

    }

    me.DeleteHolidayView = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this !",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_national_holiday,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.PV_List);
                    swal("Deleted!", "Your Category has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Category is safe :)", "error");
            }
        });
    }

    me.ShowBox_AddEmployeeLeaveType = function (param) {
        var split = param.split("::");

        var action_type = split[0];
        var leave_type_id = "";
        var leave_type_name = "";
        if (action_type === "UPDATE") {
            leave_type_id = split[1];
            leave_type_name = split[2];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_Leave_type"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='leave_type_id' name='leave_type_id' value='" + leave_type_id + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Leave Name: <small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="leave_type_name" name="leave_type_name" ' + "placeholder='Enter Leave Name' value='" + leave_type_name + "'>" + "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddEmployeeLeaveType();" class="btn btn-sm w-50 btn-success" type="button">Save Leave Type</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_emp_Leave_type").html("Add new Leave Type");
        if (split[0] === "UPDATE") {
            $("#leave_type_name").val(split[2]);
            $("#title_emp_Leave_type").html("Update Leave Type");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.AddEmployeeLeaveType = function () {
        var action_type = $("#action_type").val();
        var leave_type_id = $("#leave_type_id").val();
        var leave_type_name = $("#leave_type_name").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('leave_type_id', leave_type_id);
        formdata.append('leave_type_name', leave_type_name);


        swal({
            title: "Employee Leave Type",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_emp_leave_type,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.message);
                    if (data.message === "Success") {
                        location.reload();
                    }
                });
            } else {
                swal("Cancelled", "Please Re-check your Status :)", "error");
            }
        });

    }

    me.DeleteLeaveType = function (id) {
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this !",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_emp_leave_type,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.PV_List);
                    swal("Deleted!", "Your Leave Type has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your Leave Type is safe :)", "error");
            }
        });
    }

    me.ShowBox_AddWeeklyWorking = function (param) {
        var split = param.split("::");

        var action_type = split[0];
        var weekly_id = "";
        var cmd_schedule_id = "";
        var weekly_dayname = "";
        var start_time = "";
        var end_time = "";
        if (action_type === "UPDATE") {
            weekly_id = split[1];
            cmd_schedule_id = split[2];
            weekly_dayname = split[3];
            start_time = split[4];
            end_time = split[5];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_week_work"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='weekly_id' name='weekly_id' value='" + weekly_id + "' autocomplete='off'>" + '<label for="recipient-name" class="form-label">Working Schedule:</label>' + '<select class="form-control" name="cmd_schedule_id" id="cmd_schedule_id">' + '<option value="NA">Select Schedule</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Week Day: <small class="text-warning">*</small></label>' + '<br>' + '<select name="weekly_dayname" id="weekly_dayname" class="form-control">' + '  <option value="NA">Select Working Day</option>' + '  <option value="monday">Monday</option>' + '  <option value="tuesday">Tuesday</option>' + '  <option value="wednesday">Wednesday</option>' + '  <option value="thursday">Thursday</option>' + '  <option value="friday">Friday</option>' + '  <option value="saturday">Saturday</option>' + '  <option value="sunday">Sunday</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Start Time: <small class="text-warning">*</small></label>' + '<div class="form-group">' + '        <div class="input-group">' + '            <div class="input-group-text"><i class="typcn typcn-stopwatch tx-24 lh--9 op-6"></i></div>' + '            <input type="text" class="form-control flatpickr-input active" id="start_time" name="start_time" placeholder="Choose time"' + '                   readonly="readonly"></div>' + '</div>' + '<label for="recipient-name" class="col-form-label">End Time: <small class="text-warning">*</small></label>' + '<div class="form-group">' + '        <div class="input-group">' + '            <div class="input-group-text"><i class="typcn typcn-stopwatch tx-24 lh--9 op-6"></i></div>' + '            <input type="text" class="form-control flatpickr-input active" id="end_time" name="end_time" placeholder="Choose time"' + '                   readonly="readonly"></div>' + '</div>' + "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddWeeklyWorking();" class="btn btn-sm w-50 btn-success" type="button">Save Working Day</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#cmd_schedule_id").select();
        GlobalModelJS.FillCmdListByModel("tbl_working_schedule", "shift_name", "sche_code", "cmd_schedule_id", "");

        $("#title_emp_week_work").html("Add new Week Work");
        if (split[0] === "UPDATE") {
            $("#cmd_schedule_id").val(split[2]);
            $("#weekly_dayname").val(split[3]);
            $("#start_time").val(split[4]);
            $("#end_time").val(split[5]);
            $("#title_emp_week_work").html("Update Week Work");
        }

        //For Time Picker
        flatpickr("#start_time", {
            enableTime: true, noCalendar: true, dateFormat: "H:i",
        });

        flatpickr("#end_time", {
            enableTime: true, noCalendar: true, dateFormat: "H:i",
        });

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.AddWeeklyWorking = function () {
        var action_type = $("#action_type").val();
        var weekly_id = $("#weekly_id").val();
        var cmd_schedule_id = $("#cmd_schedule_id").val();
        var weekly_dayname = $("#weekly_dayname").val();
        var start_time = $("#start_time").val();
        var end_time = $("#end_time").val();


        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('weekly_id', weekly_id);
        formdata.append('cmd_schedule_id', cmd_schedule_id);
        formdata.append('weekly_dayname', weekly_dayname);
        formdata.append('start_time', start_time);
        formdata.append('end_time', end_time);


        swal({
            title: "Employee Weekly Working",
            text: action_type,
            type: "success",
            showCancelButton: true,
            confirmButtonClass: "btn btn-danger",
            confirmButtonText: "Yes, Confirm!",
            closeOnConfirm: false
        }, function (isConfirm) {
            if (isConfirm) {
                var paramas = {
                    url: add_weekly_working,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.message);
                    if (data.message === "Success") {
                        location.reload();
                    }
                });
            } else {
                swal("Cancelled", "Please Re-check your Status :)", "error");
            }
        });

    }

    me.DeleteWorkingScheduleView = function (id) {

        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this !",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Yes, Delete it!",
            cancelButtonText: "No, Cancel!",
            closeOnConfirm: false,
            closeOnCancel: false

        }, function (isConfirm) {
            if (isConfirm) {

                let formdata = new FormData();
                formdata.append('id', id);
                var paramas = {
                    url: delete_weekly_working,
                    data: formdata,
                    type: "POST",
                    dataType: 'json',
                    headers: {'X-CSRFToken': posttoken}
                };
                callAJAX(paramas, function (data) {
                    // console.log(data.PV_List);
                    swal("Deleted!", "Your weekly working has been deleted.", "success");
                    if (data.message === "Success") {
                        location.reload();
                    }
                });

            } else {
                swal("Cancelled", "Your weekly working is safe :)", "error");
            }
        });
    }

    //// LEAVE FUNCTION END


    ///// SINGLE EMPLOYEE LOCATION (START)
    me.ShowBox_AddEmployeeLocation = function (param) {

        var split = param.split(",");
        var action_type = split[0];
        var employee_code = split[1];
        var location_id = "";
        var cmd_location = "";
        var cmd_status = "";
        if (action_type === "UPDATE") {
            location_id = split[2];
            cmd_location = split[3];
            cmd_status = split[4];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_location"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='location_id' name='location_id' value='" + location_id + "' autocomplete='off'>" + "<input type='hidden' id='employee_code' name='employee_code' value='" + employee_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Employee Location: <small class="text-warning">*</small></label>' + '<select id="cmd_location" name="cmd_location" class="form-control form-select select2-no-search text-capitalize">' + '<option value="NA">Select Location</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Status: <small class="text-warning">*</small></label>' + '<select id="cmd_status" name="cmd_status" class="form-control form-select select2-no-search text-capitalize">' + '<option value="Active">Active</option>' + '<option value="Block">Block</option>' + '</select>' + '</div>');


        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddEmployeeLocation();" class="btn btn-sm w-50 btn-success" type="button">Save Location</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        HRMModelJS.FillCmdEmployeeLocation("cmd_location", cmd_location, employee_code, cmd_location, action_type);

        $("#title_emp_location").html("Add new Employee Location");
        if (split[0] === "UPDATE") {
            // $("#cmd_location").val(split[3]);
            $("#cmd_status").val(split[4]);
            $("#title_emp_location").html("Update Employee Location");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');


        $('#cmd_location').select2();
        $('#cmd_status').select2();


    }

    ////ADDED NEW EMPLOYEE LOCATION
    me.AddEmployeeLocation = function () {
        var action_type = $("#action_type").val();
        var location_id = $("#location_id").val();
        var cmd_location = $("#cmd_location").val();
        var cmd_status = $("#cmd_status").val();
        var employee_code = $("#employee_code").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('location_id', location_id);
        formdata.append('cmd_location', cmd_location);
        formdata.append('cmd_status', cmd_status);
        formdata.append('employee_code', employee_code);

        var paramas = {
            url: add_emp_location, data: formdata, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            $("#emp_location_body").empty("");

            var loopCount = 1;
            if (data.employee_location.length > 0) {
                for (let i = 0; i < data.employee_location.length; i++) {
                    let editParam = "UPDATE," + employee_code + "," + data.employee_location[i].id + "," + data.employee_location[i].loc_store_code_id + "," + data.employee_location[i].status;
                    $("#emp_location_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + loopCount + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.employee_location[i].name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.employee_location[i].loc_store_name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.employee_location[i].status + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_AddEmployeeLocation('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '</td>' + '</tr>');
                    loopCount++;
                }
            }

            $('#effectModal').modal('hide');
        });
    }

    // GET ONLY THOSE STORE LOCATIONS WHICH ARE NOT ADD IN SINGLE EMPLOYEE LOCATION
    me.FillCmdEmployeeLocation = function (cmd_id, selected_value, employee_code, cmd_location, action_type) {

        let formdata = new FormData();
        formdata.append('employee_code', employee_code);
        formdata.append('cmd_location', cmd_location);
        formdata.append('action_type', action_type);

        var paramas = {
            url: cmd_employee_location,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            // alert(data.cmd_list)
            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.cmd_list.length; i++) {

                sbox.add(new Option(data.cmd_list[i]["loc_store_name"], data.cmd_list[i]["loc_store_code"]));
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }
        });
    }
    ///// SINGLE EMPLOYEE LOCATION (END)

    ////SINGLE EMPLOYEE DEDUCTION FUNCTION (START)
    me.ShowBox_AddSingleEmployeeFixedDeduction = function (param) {

        var split = param.split(',');
        var action_type = split[0];
        var employee_code = split[1];
        var ded_type_code = "";
        var ded_type_name = "";
        var ded_amount = "";

        if (action_type === "UPDATE") {
            ded_type_code = split[2];
            ded_type_name = split[3];
            ded_amount = split[4];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_category"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='employee_code' name='employee_code' value='" + employee_code + "' autocomplete='off'>" + "<input type='hidden' id='ded_type_code' name='ded_type_code' value='" + ded_type_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Deduction Name<small class="text-warning">*</small></label>' + '<select name="ded_type_name" id="ded_type_name" class="form-control">' + '<option value="">Select</option></select>' + '<label for="recipient-name" class="col-form-label">Deduction Amount<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="ded_amount" name="ded_amount" placeholder="Enter Deduction Category" value="' + ded_amount + '">' + '</div>');

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddSingleEmployeeFixedDeduction();" class="btn btn-sm w-50 btn-success" type="button">Save Deduction</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        HRMModelJS.FillCmdFixedDeductionTypeName("ded_type_name", ded_type_name);

        $("#title_emp_category").html("Add New Deduction");
        if (split[0] === "UPDATE") {

            $("#ded_type_code").val(split[2]);
            $("#ded_amount").val(split[4]);
            $("#title_emp_category").html("Update Deduction");
        }
        $('#ded_type_name').select2();

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddSingleEmployeeFixedDeduction = function () {
        var action_type = $("#action_type").val();
        var employee_code = $("#employee_code").val();
        var ded_type_code = $("#ded_type_code").val();
        var ded_type_name = $("#ded_type_name").val();
        var ded_amount = $("#ded_amount").val();

        let formdata = new FormData();

        formdata.append('action_type', action_type);
        formdata.append('employee_code', employee_code);
        formdata.append('ded_type_code', ded_type_code);
        formdata.append('ded_type_name', ded_type_name);
        formdata.append('ded_amount', ded_amount);

        var paramas = {
            url: add_single_employee_fixed_deduction,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };

        callAJAX(paramas, function (data) {
            $("#fixed_deduction_body").empty("");
            // alert(data.fixed_deduction.length);
            var loopCount = 1;

            if (data.fixed_deduction.length > 0) {
                for (let i = 0; i < data.fixed_deduction.length; i++) {
                    let editParam = "UPDATE," + employee_code + "," + data.fixed_deduction[i].ded_fixed_code + "," + data.fixed_deduction[i].ded_type_code + "," + data.fixed_deduction[i].deduction_amount;
                    $("#fixed_deduction_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + loopCount + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.fixed_deduction[i].ded_type_name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.fixed_deduction[i].deduction_amount + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_AddSingleEmployeeFixedDeduction('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '</td>' + '</tr>');
                    loopCount++;
                }
            }

            $('#effectModal').modal('hide');
        });
    }

    // ADD NON FIXED DEDUCTION
    me.ShowBox_AddSingleEmployeeNonFixedDeduction = function (param) {

        var split = param.split('^^');
        var action_type = split[0];
        var employee_code = split[1];
        var ded_type_code = "";
        var ded_type_name = "";
        var payment_method = "";
        var ded_date = "";
        var ded_amount = "";


        if (action_type === "UPDATE") {
            ded_type_code = split[2];
            ded_type_name = split[3];
            payment_method = split[4];
            ded_date = split[5];
            ded_amount = split[6];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_category"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='employee_code' name='employee_code' value='" + employee_code + "' autocomplete='off'>" + "<input type='hidden' id='ded_type_code' name='ded_type_code' value='" + ded_type_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Deduction Name<small class="text-warning">*</small></label>' + '<select name="ded_type_name" id="ded_type_name" class="form-control">' + '<option value="">Select</option></select>' + '' + '<label for="recipient-name" class="col-form-label">Payment Method<small class="text-warning">*</small></label>' + '<select name="payment_method" id="payment_method" class="form-control">' + '<option value="NA">Select</option></select>' + '<label for="recipient-name" class="col-form-label">Deduction Date<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="ded_date" name="ded_date" placeholder="Enter Deduction Date" value="' + ded_date + '">' + '<label for="recipient-name" class="col-form-label">Deduction Amount<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="ded_amount" name="ded_amount" placeholder="Enter Deduction Category" value="' + ded_amount + '">' + '</div>');


        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddSingleEmployeeNonFixedDeduction();" class="btn btn-sm w-50 btn-success" type="button">Save Deduction</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        HRMModelJS.FillCmdNonFixedDeductionTypeName("ded_type_name", ded_type_name);
        HRMModelJS.FillCmdEmployeePaymentMethodList("payment_method", employee_code, payment_method);


        $("#title_emp_category").html("Add New Deduction");
        if (split[0] === "UPDATE") {

            $("#ded_type_code").val(split[2]);
            $("#ded_date").val(split[5]);
            $("#ded_amount").val(split[6]);

            $("#title_emp_category").html("Update Deduction");


        }
        $('#ded_type_name').select2();
        $('#payment_method').select2();

        flatpickr("#ded_date", {});

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddSingleEmployeeNonFixedDeduction = function () {
        var action_type = $("#action_type").val();
        var employee_code = $("#employee_code").val();
        var ded_type_code = $("#ded_type_code").val();
        var ded_type_name = $("#ded_type_name").val();
        var payment_method = $("#payment_method").val();
        var ded_date = $("#ded_date").val();
        var ded_amount = $("#ded_amount").val();


        let formdata = new FormData();

        formdata.append('action_type', action_type);
        formdata.append('employee_code', employee_code);
        formdata.append('ded_type_code', ded_type_code);
        formdata.append('ded_type_name', ded_type_name);
        formdata.append('payment_method', payment_method);
        formdata.append('ded_date', ded_date);
        formdata.append('ded_amount', ded_amount);


        var paramas = {
            url: add_single_employee_non_fixed_deduction,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };

        callAJAX(paramas, function (data) {
            $("#trans_deduction_body").empty("");
            // alert(data.fixed_deduction.length);
            var loopCount = 1;

            if (data.trans_deduction.length > 0) {
                for (let i = 0; i < data.trans_deduction.length; i++) {

                    var payment = "";
                    if (data.trans_deduction[i].pm_name === 'Cash') {
                        payment = data.trans_deduction[i].pm_name;
                    } else if (data.trans_deduction[i].pm_name === 'bank') {
                        payment = data.trans_deduction[i].pm_name + "--" + data.trans_deduction[i].bank_name;
                    } else {
                        payment = data.trans_deduction[i].pm_name + "--" + data.trans_deduction[i].account_number;
                    }
                    let editParam = "UPDATE^^" + employee_code + "^^" + data.trans_deduction[i].ded_trans_code + "^^" + data.trans_deduction[i].ded_type_code_id + "^^" + data.trans_deduction[i].payment_code_id + "^^" + data.trans_deduction[i].trans_date + "^^" + data.trans_deduction[i].trans_amount;
                    $("#trans_deduction_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + loopCount + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.trans_deduction[i].ded_type_name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.trans_deduction[i].trans_date + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + payment + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.trans_deduction[i].trans_amount + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_AddSingleEmployeeNonFixedDeduction('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '</td>' + '</tr>');
                    loopCount++;
                }
            }

            $('#effectModal').modal('hide');
        });
    }
    // CONDITION ON DEDUCTION TYPE FIXED
    me.FillCmdFixedDeductionTypeName = function (cmd_id, selected_value) {

        var paramas = {
            url: cmd_deduction_type_name, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value=''>Select Deduction Type</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i]["ded_type_name"], data.cmd_list[i]["ded_type_code"]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            } else {
                $("#" + cmd_id + "> option").removeAttr("selected");
                $('#' + cmd_id).empty();
                $('#' + cmd_id).append("<option value=''>No Record Found</option>");
            }
        });
    }
    // CONDITION ON DEDUCTION TYPE NON FIXED
    me.FillCmdNonFixedDeductionTypeName = function (cmd_id, selected_value) {

        var paramas = {
            url: cmd_non_deduction_type_name, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value='NA'>Select Deduction Type</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i]["ded_type_name"], data.cmd_list[i]["ded_type_code"]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            } else {
                $("#" + cmd_id + "> option").removeAttr("selected");
                $('#' + cmd_id).empty();
                $('#' + cmd_id).append("<option value=''>No Record Found</option>");
            }
        });
    }
    // GET ALL EMPLOYEE PAYMENT METHOD LIST
    me.FillCmdEmployeePaymentMethodList = function (cmd_id, employee_code, selected_value) {

        let formdata = new FormData();
        formdata.append('employee_code', employee_code);
        var paramas = {
            url: cmd_employee_payment_method_list,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.cmd_list.length; i++) {
                if (data.cmd_list[i]["pm_name"] === 'Cash') {
                    sbox.add(new Option(data.cmd_list[i]["pm_name"], data.cmd_list[i]["pm_code"]));
                } else if (data.cmd_list[i]["pm_name"] === 'bank') {
                    sbox.add(new Option(data.cmd_list[i]["pm_name"] + "--" + data.cmd_list[i]["bank_name"], data.cmd_list[i]["pm_code"]));
                } else {
                    sbox.add(new Option(data.cmd_list[i]["pm_name"] + "--" + data.cmd_list[i]["account_number"], data.cmd_list[i]["pm_code"]));
                }
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }
        });
    }
    ////SINGLE EMPLOYEE DEDUCTION FUNCTION (END)


    // //SINGLE EMPLOYEE ALLOWANCE FUNCTION (START)
    me.ShowBox_AddSingleEmployeeFixedAllowance = function (param) {

        var split = param.split(',');
        var action_type = split[0];
        var employee_code = split[1];
        var all_type_code = "";
        var all_type_name = "";
        var all_amount = "";

        if (action_type === "UPDATE") {
            all_type_code = split[2];
            all_type_name = split[3];
            all_amount = split[4];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='employee_code' name='employee_code' value='" + employee_code + "' autocomplete='off'>" + "<input type='hidden' id='all_type_code' name='all_type_code' value='" + all_type_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Allowance Name<small class="text-warning">*</small></label>' + '<select name="all_type_name" id="all_type_name" class="form-control">' + '<option value="">Select</option></select>' + '<label for="recipient-name" class="col-form-label">Allowance Amount<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="all_amount" name="all_amount" placeholder="Enter Allowance Amount" value="' + all_amount + '">' + '</div>');

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddSingleEmployeeFixedAllowance();" class="btn btn-sm w-50 btn-success" type="button">Save Allowance</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        HRMModelJS.FillCmdFixedAllowanceTypeName("all_type_name", all_type_name);

        $("#title").html("Add New Allowance");
        if (split[0] === "UPDATE") {
            $("#all_type_code").val(split[2]);
            $("#all_amount").val(split[4]);

            $("#title").html("Update Allowance");
        }
        $('#all_type_name').select2();

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddSingleEmployeeFixedAllowance = function () {
        var action_type = $("#action_type").val();
        var employee_code = $("#employee_code").val();
        var all_type_code = $("#all_type_code").val();
        var all_type_name = $("#all_type_name").val();
        var all_amount = $("#all_amount").val();

        let formdata = new FormData();

        formdata.append('action_type', action_type);
        formdata.append('employee_code', employee_code);
        formdata.append('all_type_code', all_type_code);
        formdata.append('all_type_name', all_type_name);
        formdata.append('all_amount', all_amount);

        var paramas = {
            url: add_single_employee_fixed_allowance,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            $("#fixed_allowance_body").empty("");

            var loopCount = 1;

            if (data.fixed_allowance.length > 0) {
                for (let i = 0; i < data.fixed_allowance.length; i++) {
                    let editParam = "UPDATE," + employee_code + "," + data.fixed_allowance[i].all_fixed_code + "," + data.fixed_allowance[i].all_type_code + "," + data.fixed_allowance[i].allowance_amount;
                    $("#fixed_allowance_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + loopCount + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.fixed_allowance[i].all_type_name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.fixed_allowance[i].allowance_amount + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_AddSingleEmployeeFixedAllowance('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '</td>' + '</tr>');
                    loopCount++;
                }
            }
            $('#effectModal').modal('hide');
        });
    }

    // SHOW DROPDOWN FOR FIXED ALLOWANCE
    me.FillCmdFixedAllowanceTypeName = function (cmd_id, selected_value) {

        var paramas = {
            url: cmd_fixed_allowance_type_name, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value=''>Select Allowance Type</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i]["all_type_name"], data.cmd_list[i]["all_type_code"]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            } else {
                $("#" + cmd_id + "> option").removeAttr("selected");
                $('#' + cmd_id).empty();
                $('#' + cmd_id).append("<option value=''>No Record Found</option>");
            }
        });
    }

    // ADD NON FIXED ALLOWANCE
    me.ShowBox_AddSingleEmployeeNonFixedAllowance = function (param) {

        var split = param.split('^^');
        var action_type = split[0];
        var employee_code = split[1];
        var all_type_code = "";
        var all_type_name = "";
        var payment_method = "";
        var all_date = "";
        var all_amount = "";

        if (action_type === "UPDATE") {
            all_type_code = split[2];
            all_type_name = split[3];
            payment_method = split[4];
            all_date = split[5];
            all_amount = split[6];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" + "<input type='hidden' id='employee_code' name='employee_code' value='" + employee_code + "' autocomplete='off'>" + "<input type='hidden' id='all_type_code' name='all_type_code' value='" + all_type_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Allowance Name<small class="text-warning">*</small></label>' + '<select name="all_type_name" id="all_type_name" class="form-control">' + '<option value="">Select</option></select>' + '<label for="recipient-name" class="col-form-label">Payment Method<small class="text-warning">*</small></label>' + '<select name="payment_method" id="payment_method" class="form-control">' + '<option value="NA">Select</option></select>' + '<label for="recipient-name" class="col-form-label">Allowance Date<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="all_date" name="all_date" placeholder="Enter Allowance Date" value="' + all_date + '">' + '<label for="recipient-name" class="col-form-label">Allowance Amount<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="all_amount" name="all_amount" placeholder="Enter Allowance Amount" value="' + all_amount + '">' + '</div>');

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.AddSingleEmployeeNonFixedAllowance();" class="btn btn-sm w-50 btn-success" type="button">Save Allowance</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        HRMModelJS.FillCmdNonFixedAllowanceTypeName("all_type_name", all_type_name);
        HRMModelJS.FillCmdEmployeePaymentMethodList("payment_method", employee_code, payment_method);

        $("#title").html("Add New Allowance");
        if (split[0] === "UPDATE") {
            $("#all_type_code").val(split[2]);
            $("#all_date").val(split[5]);
            $("#all_amount").val(split[6]);
            $("#title").html("Update Allowance");
        }
        $('#all_type_name').select2();
        $('#payment_method').select2();

        flatpickr("#all_date", {});

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddSingleEmployeeNonFixedAllowance = function () {
        var action_type = $("#action_type").val();
        var employee_code = $("#employee_code").val();
        var all_type_code = $("#all_type_code").val();
        var all_type_name = $("#all_type_name").val();
        var payment_method = $("#payment_method").val();
        var all_date = $("#all_date").val();
        var all_amount = $("#all_amount").val();

        let formdata = new FormData();

        formdata.append('action_type', action_type);
        formdata.append('employee_code', employee_code);
        formdata.append('all_type_code', all_type_code);
        formdata.append('all_type_name', all_type_name);
        formdata.append('payment_method', payment_method);
        formdata.append('all_date', all_date);
        formdata.append('all_amount', all_amount);

        var paramas = {
            url: add_single_employee_non_fixed_allowance,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };

        callAJAX(paramas, function (data) {
            $("#trans_allowance_body").empty("");

            var loopCount = 1;

            if (data.trans_allowance.length > 0) {
                for (let i = 0; i < data.trans_allowance.length; i++) {

                    var payment = "";
                    if (data.trans_allowance[i].pm_name === 'Cash') {
                        payment = data.trans_allowance[i].pm_name;
                    } else if (data.trans_allowance[i].pm_name === 'bank') {
                        payment = data.trans_allowance[i].pm_name + "--" + data.trans_allowance[i].bank_name;
                    } else {
                        payment = data.trans_allowance[i].pm_name + "--" + data.trans_allowance[i].account_number;
                    }

                    let editParam = "UPDATE^^" + employee_code + "^^" + data.trans_allowance[i].all_trans_code + "^^" + data.trans_allowance[i].all_type_code_id + "^^" + data.trans_allowance[i].payment_code_id + "^^" + data.trans_allowance[i].trans_date + "^^" + data.trans_allowance[i].trans_amount;
                    $("#trans_allowance_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + loopCount + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.trans_allowance[i].all_type_name + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.trans_allowance[i].trans_date + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + payment + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center" id="status"><span> ' + data.trans_allowance[i].trans_amount + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_AddSingleEmployeeNonFixedAllowance('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '</td>' + '</tr>');
                    loopCount++;
                }
            }

            $('#effectModal').modal('hide');
        });
    }

    //SHOW NON FIXED ALLOWANCE IN DROPDOWN
    me.FillCmdNonFixedAllowanceTypeName = function (cmd_id, selected_value) {


        var paramas = {
            url: cmd_non_allowance_type_name, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value=''>Select</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i]["all_type_name"], data.cmd_list[i]["all_type_code"]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            } else {
                $("#" + cmd_id + "> option").removeAttr("selected");
                $('#' + cmd_id).empty();
                $('#' + cmd_id).append("<option value=''>No Record Found</option>");
            }
        });
    }
    // //SINGLE EMPLOYEE ALLOWANCE FUNCTION (END)

    ///// SINGLE EMPLOYEE SALARY (START)
    me.ShowBox_UpdateSingleEmployeeSalary = function (param) {

        var split = param.split('^^');
        var employee_code = split[0];
        var salary_code = split[1];
        var get_pay_frequency = split[2];
        var get_rate_type = split[3];
        var rate_amount = split[4];
        var basic_salary = split[5];
        var condition = split[6];

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_emp_category"></h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' + "<input type='hidden' id='employee_code' name='employee_code' value='" + employee_code + "' autocomplete='off'>" + "<input type='hidden' id='condition' name='condition' value='" + condition + "' autocomplete='off'>" + "<input type='hidden' id='salary_code' name='salary_code' value='" + salary_code + "' autocomplete='off'>" + '<label for="recipient-name" class="col-form-label">Pay Frequency<small class="text-warning">*</small></label>' + '<select name="cmd_pay_freguency" id="cmd_pay_freguency" class="form-control">' + '<option value="NA">Select</option>' + '<option value="monthly">Monthly</option>' + '<option value="weekly">Weekly</option>' + '<option value="daily">Daily</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Rate Type<small class="text-warning">*</small></label>' + '<select name="cmd_rate_type" id="cmd_rate_type" class="form-control">' + '<option value="NA">Select</option>' + '<option value="salary" id="Salary">Salary</option>' + '<option value="hourly">Hourly</option>' + '<option value="wages">Wages</option>' + '</select>' + '<label for="recipient-name" class="col-form-label">Rate Amount<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="rate_amount" name="rate_amount" placeholder="Enter Deduction Category" value="' + rate_amount + '">' + '<label for="recipient-name" class="col-form-label">Basic Salary<small class="text-warning">*</small></label>' + '<input type="text" class="form-control" id="basic_salary" name="basic_salary" placeholder="Enter Deduction Category" value="' + basic_salary + '">' + '</div>');


        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="HRMModelJS.UpdateSingleEmployeeSalary();" class="btn btn-sm w-50 btn-success" type="button">Update Salary</button>' + '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        HRMModelJS.conditionPayRate(get_pay_frequency, get_rate_type);

        $("#cmd_pay_freguency").change(function (e) {
            get_pay_frequency = e.target.value;
            HRMModelJS.conditionPayRate(get_pay_frequency, get_rate_type);

            $("#cmd_rate_type").change(function (e) {
                get_rate_type = e.target.value;
                HRMModelJS.conditionPayRate(get_pay_frequency, get_rate_type);
            });
        });

        $("#cmd_pay_freguency").val(split[2]);
        $("#cmd_rate_type").val(split[3]);
        $("#title_emp_category").html("Update Salary");
        // Select2
        $('#cmd_pay_freguency').select2();
        $('#cmd_rate_type').select2();

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.conditionPayRate = function (get_pay_frequency, get_rate_type) {
        $("#rate_amount").prop('readonly', false);
        $("#basic_salary").prop('readonly', false);

        if (get_pay_frequency === "monthly" && get_rate_type === "salary") {
            $("#rate_amount").val("0");
            $("#rate_amount").prop('readonly', true);
        }
        if (get_pay_frequency === "monthly" && get_rate_type === "hourly") {
            $("#basic_salary").val("0");
            $("#basic_salary").prop('readonly', true);
        }
        if (get_pay_frequency === "weekly" && get_rate_type === "salary") {
            $("#rate_amount").val("0");
            $("#rate_amount").prop('readonly', true);
        }
        if (get_pay_frequency === "weekly" && get_rate_type === "hourly") {
            $("#basic_salary").val("0");
            $("#basic_salary").prop('readonly', true);
        }
        if (get_pay_frequency === "daily" && get_rate_type === "hourly") {
            $("#basic_salary").val("0");
            $("#basic_salary").prop('readonly', true);
        }
        if (get_pay_frequency === "daily" && get_rate_type === "salary") {
            $("#rate_amount").val("0");
            $("#rate_amount").prop('readonly', true);
            $("#basic_salary").val("0");
            $("#basic_salary").prop('readonly', true);
        } else if (get_rate_type === "wages") {
            $("#rate_amount").val("0");
            $("#rate_amount").prop('readonly', true);
            $("#basic_salary").val("0");
            $("#basic_salary").prop('readonly', true);
        }
    }

    me.UpdateSingleEmployeeSalary = function () {

        var employee_code = $("#employee_code").val();
        var salary_code = $("#salary_code").val();
        var get_pay_frequency = $("#cmd_pay_freguency").val();
        var get_rate_type = $("#cmd_rate_type").val();
        var rate_amount = $("#rate_amount").val();
        var basic_salary = $("#basic_salary").val();
        var condition = $("#condition").val();

        let formdata = new FormData();

        formdata.append('employee_code', employee_code);
        formdata.append('salary_code', salary_code);
        formdata.append('get_pay_frequency', get_pay_frequency);
        formdata.append('get_rate_type', get_rate_type);
        formdata.append('rate_amount', rate_amount);
        formdata.append('basic_salary', basic_salary);

        var paramas = {
            url: update_single_employee_salary,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };

        callAJAX(paramas, function (data) {
            if (condition === "Multiple") {
                location.reload();
            }
            if (condition === "Single") {

                $("#emp_salary_body").empty("");
                // alert(data.employee_salary.length);
                var loopCount = 1;

                if (data.employee_salary.length > 0) {
                    for (let i = 0; i < data.employee_salary.length; i++) {

                        let editParam = employee_code + "^^" + data.employee_salary[i].salary_code + "^^" + data.employee_salary[i].pay_frequency + "^^" + data.employee_salary[i].rate_type + "^^" + data.employee_salary[i].rate_amount + "^^" + data.employee_salary[i].basic_salary + "^^Single";
                        $("#emp_salary_body").append('<tr>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.employee_salary[i].pay_frequency + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center"><span> ' + data.employee_salary[i].rate_type + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center"><span> ' + data.employee_salary[i].rate_amount + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center"><span> ' + data.employee_salary[i].basic_salary + '</span></td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<button class="btn btn-sm btn-def tx-muted" ' + "onclick=HRMModelJS.ShowBox_UpdateSingleEmployeeSalary('" + editParam + "');>" + '<i class="fe fe-edit"></i>' + '</button>' + '</td>' + '</tr>');
                        loopCount++;
                    }
                }
                swal.close();
                $('#effectModal').modal('hide');

            }
        });
    }
    ///// SINGLE EMPLOYEE SALARY (START)

    //MULTIPLE FIXED DEDUCTION(START)
    me.AddMultiplteEmployeeFixedDeduction = function (selected_employee) {

        employee_code_and_name = selected_employee.split('^^');
        employee_code = employee_code_and_name[0];
        employee_name = employee_code_and_name[1];

        $("#add_row_for_deduction").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_ded_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_ded_type[]" onchange=HRMModelJS.OnChangeValues_AddFixedDeduction("' + me.selItemCount + '")>' + '<option value="">Select Deduction Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="ded_amount_' + me.selItemCount + '" name="ded_amount[]" placeholder="Enter Deduction Amount" class="form-control text-center" oninput=HRMModelJS.OnChangeValues_AddFixedDeduction("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeFixedDeductionDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

        $("#cmd_fixed_ded_type_" + me.selItemCount).select2();
        HRMModelJS.FillCmdFixedDeductionTypeName("cmd_fixed_ded_type_" + me.selItemCount, "");

        me.Employee_OBJ.push({
            sl: me.selItemCount, employee_code: employee_code, employee_name: employee_name, ded_type: "", ded_amount: 0
        });

        me.selItemCount++;
        $("#cmd_employee").val("NA"); // Select the option with a value of '1'
        $("#cmd_employee").trigger('change'); // Notify any JS components that the value changed

        me.SingleItem_BoxAddFixedDeduction();

    }

    me.OnChangeValues_AddFixedDeduction = function (selected_index) {

        let ded_type = $("#cmd_fixed_ded_type_" + selected_index).val();
        let ded_amount = $("#ded_amount_" + selected_index).val();


        for (var m = 0; m < me.Employee_OBJ.length; m++) {
            if (me.Employee_OBJ[m].sl === parseInt(selected_index)) {
                me.Employee_OBJ[m].ded_type = ded_type;
                me.Employee_OBJ[m].ded_amount = ded_amount;
            }
        }
        me.SingleItem_BoxAddFixedDeduction();
    }

    me.SingleItem_BoxAddFixedDeduction = function () {

        let strEmployeeCode = "";
        let strDedType = "";
        let strDedAmount = "";
        let count = 1;

        if (me.Employee_OBJ.length === 1) {
            strEmployeeCode = me.Employee_OBJ[0].employee_code;
            strDedType = me.Employee_OBJ[0].ded_type;
            strDedAmount = me.Employee_OBJ[0].ded_amount;

        }
        if (me.Employee_OBJ.length > 1) {
            strEmployeeCode = "";
            strDedType = "";
            strDedAmount = "";
            for (var p = 0; p < me.Employee_OBJ.length; p++) {
                if (count === 1) {
                    strEmployeeCode = me.Employee_OBJ[p].employee_code + "^";
                    strDedType = me.Employee_OBJ[p].ded_type + "^";
                    strDedAmount = me.Employee_OBJ[p].ded_amount + "^";
                }
                if (count > 1 && count < me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code + "^";
                    strDedType = strDedType + "" + me.Employee_OBJ[p].ded_type + "^";
                    strDedAmount = strDedAmount + "" + me.Employee_OBJ[p].ded_amount + "^";
                }
                if (count === me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code;
                    strDedType = strDedType + "" + me.Employee_OBJ[p].ded_type;
                    strDedAmount = strDedAmount + "" + me.Employee_OBJ[p].ded_amount;

                }
                count++;
            } // LOOP END
        } // MORE THAN ONE ROW

        $("#row_length").val(me.Employee_OBJ.length);
        $("#str_employee_code").val(strEmployeeCode);
        $("#str_ded_type").val(strDedType);
        $("#str_ded_amount").val(strDedAmount);

    }

    me.onClickEmployeeFixedDeductionDelete = function (index) {
        let deletedIndex = parseInt(index);

        CheckObj = me.Employee_OBJ;

        me.selItemCount = 1;
        $("#add_row_for_deduction").html("");

        me.Employee_OBJ = [];
        for (var p = 0; p < CheckObj.length; p++) {
            if (CheckObj[p].sl !== deletedIndex) {

                $("#add_row_for_deduction").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + CheckObj[p].employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + CheckObj[p].employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_ded_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_ded_type[]" onchange=HRMModelJS.OnChangeValues_AddFixedDeduction("' + me.selItemCount + '")>' + '<option value="">Select Deduction Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="ded_amount_' + me.selItemCount + '" name="ded_amount[]" placeholder="Enter Deduction Amount" class="form-control text-center"  value="' + CheckObj[p].ded_amount + '" oninput=HRMModelJS.OnChangeValues_AddFixedDeduction("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeFixedDeductionDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

                $("#cmd_fixed_ded_type_" + me.selItemCount).select2();
                HRMModelJS.FillCmdFixedDeductionTypeName("cmd_fixed_ded_type_" + me.selItemCount, CheckObj[p].ded_type);

                me.Employee_OBJ.push({
                    sl: me.selItemCount,
                    employee_code: CheckObj[p].employee_code,
                    employee_name: CheckObj[p].employee_name,
                    ded_type: CheckObj[p].ded_type,
                    ded_amount: CheckObj[p].ded_amount
                });

                me.selItemCount++
            } // CONDITION END
        } // LOOP END

        me.SingleItem_BoxAddFixedDeduction();

    }
    //MULTIPLE FIXED DEDUCTION(END)

    //MULTIPLE NON FIXED DEDUCTION(START)
    me.AddMultiplteEmployeeNonFixedDeduction = function (selected_employee) {

        employee_code_and_name = selected_employee.split('^^');
        employee_code = employee_code_and_name[0];
        employee_name = employee_code_and_name[1];

        $("#add_row_for_nonfixed_deduction").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_ded_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_ded_type[]" onchange=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")>' + '<option value="NA">Select Deduction Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_payment_method_' + me.selItemCount + '" class="form-control" name="cmd_payment_method[]" onchange=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")>' + '<option value="NA">Select Payment Method</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="ded_amount_' + me.selItemCount + '" name="ded_amount[]" placeholder="Enter Deduction Amount" class="form-control text-center" oninput=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="text" id="ded_date_' + me.selItemCount + '" name="ded_date[]" placeholder="Enter Deduction Date" class="form-control text-center" oninput=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeNonFixedDeductionDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

        $("#cmd_fixed_ded_type_" + me.selItemCount).select2();
        $("#cmd_payment_method_" + me.selItemCount).select2();
        flatpickr("#ded_date_" + me.selItemCount, {});
        HRMModelJS.FillCmdNonFixedDeductionTypeName("cmd_fixed_ded_type_" + me.selItemCount, "");
        HRMModelJS.FillCmdEmployeePaymentMethodList("cmd_payment_method_" + me.selItemCount, employee_code, "");

        me.Employee_OBJ.push({
            sl: me.selItemCount,
            employee_code: employee_code,
            employee_name: employee_name,
            ded_type: "NA",
            payment_method: "NA",
            ded_amount: '',
            ded_date: ''
        });
        me.selItemCount++;

        $("#cmd_employee").val("NA"); // Select the option with a value of '1'
        $("#cmd_employee").trigger('change'); // Notify any JS components that the value changed

        me.SingleItem_BoxNonFixedDeduction();
    }

    me.OnChangeValues_NonFixedDeduction = function (selected_index) {

        let ded_type = $("#cmd_fixed_ded_type_" + selected_index).val();
        let payment_method = $("#cmd_payment_method_" + selected_index).val();
        let ded_amount = $("#ded_amount_" + selected_index).val();
        let ded_date = $("#ded_date_" + selected_index).val();


        for (var m = 0; m < me.Employee_OBJ.length; m++) {
            if (me.Employee_OBJ[m].sl === parseInt(selected_index)) {
                me.Employee_OBJ[m].ded_type = ded_type;
                me.Employee_OBJ[m].payment_method = payment_method;
                me.Employee_OBJ[m].ded_amount = ded_amount;
                me.Employee_OBJ[m].ded_date = ded_date;
            }
        }
        me.SingleItem_BoxNonFixedDeduction();
    }

    me.SingleItem_BoxNonFixedDeduction = function () {

        let strEmployeeCode = "";
        let strDedType = "";
        let strPaymentMethod = "";
        let strDedAmount = "";
        let strDedDate = "";
        let count = 1;

        if (me.Employee_OBJ.length === 1) {
            strEmployeeCode = me.Employee_OBJ[0].employee_code;
            strDedType = me.Employee_OBJ[0].ded_type;
            strPaymentMethod = me.Employee_OBJ[0].payment_method;
            strDedAmount = me.Employee_OBJ[0].ded_amount;
            strDedDate = me.Employee_OBJ[0].ded_date;

        }
        if (me.Employee_OBJ.length > 1) {
            strEmployeeCode = "";
            strDedType = "";
            strPaymentMethod = "";
            strDedAmount = "";
            strDedDate = "";
            for (var p = 0; p < me.Employee_OBJ.length; p++) {
                if (count === 1) {
                    strEmployeeCode = me.Employee_OBJ[p].employee_code + "^";
                    strDedType = me.Employee_OBJ[p].ded_type + "^";
                    strPaymentMethod = me.Employee_OBJ[p].payment_method + "^";
                    strDedAmount = me.Employee_OBJ[p].ded_amount + "^";
                    strDedDate = me.Employee_OBJ[p].ded_date + "^";
                }
                if (count > 1 && count < me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code + "^";
                    strDedType = strDedType + "" + me.Employee_OBJ[p].ded_type + "^";
                    strPaymentMethod = strPaymentMethod + "" + me.Employee_OBJ[p].payment_method + "^";
                    strDedAmount = strDedAmount + "" + me.Employee_OBJ[p].ded_amount + "^";
                    strDedDate = strDedDate + "" + me.Employee_OBJ[p].ded_date + "^";
                }
                if (count === me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code;
                    strDedType = strDedType + "" + me.Employee_OBJ[p].ded_type;
                    strPaymentMethod = strPaymentMethod + "" + me.Employee_OBJ[p].payment_method;
                    strDedAmount = strDedAmount + "" + me.Employee_OBJ[p].ded_amount;
                    strDedDate = strDedDate + "" + me.Employee_OBJ[p].ded_date;

                }
                count++;
            } // LOOP END
        } // MORE THAN ONE ROW

        $("#row_length").val(me.Employee_OBJ.length);
        $("#str_employee_code").val(strEmployeeCode);
        $("#str_payment_method").val(strPaymentMethod);
        $("#str_ded_type").val(strDedType);
        $("#str_ded_amount").val(strDedAmount);
        $("#str_ded_date").val(strDedDate);

    }

    me.onClickEmployeeNonFixedDeductionDelete = function (index) {
        let deletedIndex = parseInt(index);

        CheckObj = me.Employee_OBJ;

        me.selItemCount = 1;
        $("#add_row_for_nonfixed_deduction").html("");

        me.Employee_OBJ = [];
        for (var p = 0; p < CheckObj.length; p++) {
            if (CheckObj[p].sl !== deletedIndex) {

                $("#add_row_for_nonfixed_deduction").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + CheckObj[p].employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + CheckObj[p].employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_ded_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_ded_type[]"  onchange=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")>' + '<option value="NA">Select Deduction Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_payment_method_' + me.selItemCount + '" class="form-control" name="cmd_payment_method[]" onchange=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")>' + '<option value="NA">Select Payment Method</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="ded_amount_' + me.selItemCount + '" name="ded_amount[]" placeholder="Enter Deduction Amount" class="form-control text-center" value="' + CheckObj[p].ded_amount + '" oninput=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="text" id="ded_date_' + me.selItemCount + '" name="ded_date[]" placeholder="Enter Deduction Date" class="form-control text-center" value="' + CheckObj[p].ded_date + '" oninput=HRMModelJS.OnChangeValues_NonFixedDeduction("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeNonFixedDeductionDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

                $("#cmd_fixed_ded_type_" + me.selItemCount).select2();
                $("#cmd_payment_method_" + me.selItemCount).select2();
                flatpickr("#ded_date_" + me.selItemCount, {});
                HRMModelJS.FillCmdNonFixedDeductionTypeName("cmd_fixed_ded_type_" + me.selItemCount, CheckObj[p].ded_type);
                HRMModelJS.FillCmdEmployeePaymentMethodList("cmd_payment_method_" + me.selItemCount, CheckObj[p].employee_code, CheckObj[p].payment_method);

                me.Employee_OBJ.push({
                    sl: me.selItemCount,
                    employee_code: CheckObj[p].employee_code,
                    employee_name: CheckObj[p].employee_name,
                    ded_type: CheckObj[p].ded_type,
                    payment_method: CheckObj[p].payment_method,
                    ded_amount: CheckObj[p].ded_amount,
                    ded_date: CheckObj[p].ded_date
                });

                me.selItemCount++
            } // CONDITION END
        } // LOOP END

        me.SingleItem_BoxNonFixedDeduction();

    }
    //MULTIPLE NON FIXED DEDUCTION(END)


    //MULTIPLE FIXED ALLOWANCE(START)
    me.AddMultiplteEmployeeFixedAllowance = function (selected_employee) {

        employee_code_and_name = selected_employee.split('^^');
        employee_code = employee_code_and_name[0];
        employee_name = employee_code_and_name[1];

        $("#add_row_for_allowance").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_all_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_all_type[]" onchange=HRMModelJS.OnChangeValues_FixedAllowance("' + me.selItemCount + '")>' + '<option value="">Select Allowance Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="all_amount_' + me.selItemCount + '" name="all_amount[]" placeholder="Enter Allowance Amount" class="form-control text-center" oninput=HRMModelJS.OnChangeValues_FixedAllowance("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeFixedAllowanceDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

        $("#cmd_fixed_all_type_" + me.selItemCount).select2();
        HRMModelJS.FillCmdFixedAllowanceTypeName("cmd_fixed_all_type_" + me.selItemCount, "");

        me.Employee_OBJ.push({
            sl: me.selItemCount, employee_code: employee_code, employee_name: employee_name, all_type: "", all_amount: 0
        });
        me.selItemCount++;

        $("#cmd_employee").val("NA"); // Select the option with a value of '1'
        $("#cmd_employee").trigger('change'); // Notify any JS components that the value changed

        me.SingleItem_BoxFixedAllowance();

    }

    me.OnChangeValues_FixedAllowance = function (selected_index) {

        let all_type = $("#cmd_fixed_all_type_" + selected_index).val();
        let all_amount = $("#all_amount_" + selected_index).val();

        for (var m = 0; m < me.Employee_OBJ.length; m++) {
            if (me.Employee_OBJ[m].sl === parseInt(selected_index)) {
                me.Employee_OBJ[m].all_type = all_type;
                me.Employee_OBJ[m].all_amount = all_amount;
            }
        }
        me.SingleItem_BoxFixedAllowance();
    }

    me.SingleItem_BoxFixedAllowance = function () {

        let strEmployeeCode = "";
        let strAllType = "";
        let strAllAmount = "";
        let count = 1;

        if (me.Employee_OBJ.length === 1) {
            strEmployeeCode = me.Employee_OBJ[0].employee_code;
            strAllType = me.Employee_OBJ[0].all_type;
            strAllAmount = me.Employee_OBJ[0].all_amount;

        }
        if (me.Employee_OBJ.length > 1) {
            strEmployeeCode = "";
            strAllType = "";
            strAllAmount = "";
            for (var p = 0; p < me.Employee_OBJ.length; p++) {
                if (count === 1) {
                    strEmployeeCode = me.Employee_OBJ[p].employee_code + "^";
                    strAllType = me.Employee_OBJ[p].all_type + "^";
                    strAllAmount = me.Employee_OBJ[p].all_amount + "^";
                }
                if (count > 1 && count < me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code + "^";
                    strAllType = strAllType + "" + me.Employee_OBJ[p].all_type + "^";
                    strAllAmount = strAllAmount + "" + me.Employee_OBJ[p].all_amount + "^";
                }
                if (count === me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code;
                    strAllType = strAllType + "" + me.Employee_OBJ[p].all_type;
                    strAllAmount = strAllAmount + "" + me.Employee_OBJ[p].all_amount;

                }
                count++;
            } // LOOP END
        } // MORE THAN ONE ROW

        $("#row_length").val(me.Employee_OBJ.length);
        $("#str_employee_code").val(strEmployeeCode);
        $("#str_all_type").val(strAllType);
        $("#str_all_amount").val(strAllAmount);

    }

    me.onClickEmployeeFixedAllowanceDelete = function (index) {
        let deletedIndex = parseInt(index);

        CheckObj = me.Employee_OBJ;

        me.selItemCount = 1;
        $("#add_row_for_allowance").html("");

        me.Employee_OBJ = [];
        for (var p = 0; p < CheckObj.length; p++) {
            if (CheckObj[p].sl !== deletedIndex) {

                $("#add_row_for_allowance").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + CheckObj[p].employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + CheckObj[p].employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_all_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_all_type[]" onchange=HRMModelJS.OnChangeValues_FixedAllowance("' + me.selItemCount + '")>' + '' + '<option value="">Select Allowance Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="all_amount_' + me.selItemCount + '" name="all_amount[]" placeholder="Enter Allowance Amount" class="form-control text-center"  value="' + CheckObj[p].all_amount + '" oninput=HRMModelJS.OnChangeValues_FixedAllowance("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeFixedAllowanceDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

                $("#cmd_fixed_all_type_" + me.selItemCount).select2();
                HRMModelJS.FillCmdFixedAllowanceTypeName("cmd_fixed_all_type_" + me.selItemCount, CheckObj[p].all_type);

                me.Employee_OBJ.push({
                    sl: me.selItemCount,
                    employee_code: CheckObj[p].employee_code,
                    employee_name: CheckObj[p].employee_name,
                    all_type: CheckObj[p].all_type,
                    all_amount: CheckObj[p].all_amount
                });

                me.selItemCount++
            } // CONDITION END
        } // LOOP END

        me.SingleItem_BoxFixedAllowance();

    }
    //MULTIPLE FIXED ALLOWANCE(END)


    //MULTIPLE NON FIXED ALLOWANCE(START)
    me.AddMultiplteEmployeeNonFixedAllowance = function (selected_employee) {

        employee_code_and_name = selected_employee.split('^^');
        employee_code = employee_code_and_name[0];
        employee_name = employee_code_and_name[1];

        $("#add_row_for_nonfixed_allowance").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_all_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_all_type[]" onchange=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")>' + '<option value="">Select Allowance Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_payment_method_' + me.selItemCount + '" class="form-control" name="cmd_payment_method[]" onchange=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")>' + '<option value="NA">Select Payment Method</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="all_amount_' + me.selItemCount + '" name="all_amount[]" placeholder="Enter Allowance Amount" class="form-control text-center" oninput=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="text" id="all_date_' + me.selItemCount + '" name="all_date[]" placeholder="Enter Allowance Date" class="form-control text-center" oninput=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeNonFixedAllowanceDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');

        $("#cmd_fixed_all_type_" + me.selItemCount).select2();
        $("#cmd_payment_method_" + me.selItemCount).select2();
        flatpickr("#all_date_" + me.selItemCount, {});
        HRMModelJS.FillCmdNonFixedAllowanceTypeName("cmd_fixed_all_type_" + me.selItemCount, "");
        HRMModelJS.FillCmdEmployeePaymentMethodList("cmd_payment_method_" + me.selItemCount, employee_code, "");

        me.Employee_OBJ.push({
            sl: me.selItemCount,
            employee_code: employee_code,
            employee_name: employee_name,
            all_type: "",
            payment_method: "NA",
            all_amount: '',
            dall_date: ''
        });
        me.selItemCount++;

        $("#cmd_employee").val("NA"); // Select the option with a value of '1'
        $("#cmd_employee").trigger('change'); // Notify any JS components that the value changed

        me.SingleItem_BoxNonFixedAllowance();
    }

    me.OnChangeValues_NonFixedAllowance = function (selected_index) {

        let all_type = $("#cmd_fixed_all_type_" + selected_index).val();
        let payment_method = $("#cmd_payment_method_" + selected_index).val();
        let all_amount = $("#all_amount_" + selected_index).val();
        let all_date = $("#all_date_" + selected_index).val();

        for (var m = 0; m < me.Employee_OBJ.length; m++) {
            if (me.Employee_OBJ[m].sl === parseInt(selected_index)) {
                me.Employee_OBJ[m].all_type = all_type;
                me.Employee_OBJ[m].payment_method = payment_method;
                me.Employee_OBJ[m].all_amount = all_amount;
                me.Employee_OBJ[m].all_date = all_date;
            }
        }
        me.SingleItem_BoxNonFixedAllowance();
    }

    me.SingleItem_BoxNonFixedAllowance = function () {

        let strEmployeeCode = "";
        let strAllType = "";
        let strPaymentMethod = "";
        let strAllAmount = "";
        let strAllDate = "";
        let count = 1;

        if (me.Employee_OBJ.length === 1) {
            strEmployeeCode = me.Employee_OBJ[0].employee_code;
            strAllType = me.Employee_OBJ[0].all_type;
            strPaymentMethod = me.Employee_OBJ[0].payment_method;
            strAllAmount = me.Employee_OBJ[0].all_amount;
            strAllDate = me.Employee_OBJ[0].all_date;

        }
        if (me.Employee_OBJ.length > 1) {
            strEmployeeCode = "";
            strAllType = "";
            strPaymentMethod = "";
            strAllAmount = "";
            strAllDate = "";
            for (var p = 0; p < me.Employee_OBJ.length; p++) {
                if (count === 1) {
                    strEmployeeCode = me.Employee_OBJ[p].employee_code + "^";
                    strAllType = me.Employee_OBJ[p].all_type + "^";
                    strPaymentMethod = me.Employee_OBJ[p].payment_method + "^";
                    strAllAmount = me.Employee_OBJ[p].all_amount + "^";
                    strAllDate = me.Employee_OBJ[p].all_date + "^";
                }
                if (count > 1 && count < me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code + "^";
                    strAllType = strAllType + "" + me.Employee_OBJ[p].all_type + "^";
                    strPaymentMethod = strPaymentMethod + "" + me.Employee_OBJ[p].payment_method + "^";
                    strAllAmount = strAllAmount + "" + me.Employee_OBJ[p].all_amount + "^";
                    strAllDate = strAllDate + "" + me.Employee_OBJ[p].all_date + "^";
                }
                if (count === me.Employee_OBJ.length) {
                    strEmployeeCode = strEmployeeCode + "" + me.Employee_OBJ[p].employee_code;
                    strAllType = strAllType + "" + me.Employee_OBJ[p].all_type;
                    strPaymentMethod = strPaymentMethod + "" + me.Employee_OBJ[p].payment_method;
                    strAllAmount = strAllAmount + "" + me.Employee_OBJ[p].all_amount;
                    strAllDate = strAllDate + "" + me.Employee_OBJ[p].all_date;

                }
                count++;
            } // LOOP END
        } // MORE THAN ONE ROW

        $("#row_length").val(me.Employee_OBJ.length);
        $("#str_employee_code").val(strEmployeeCode);
        $("#str_payment_method").val(strPaymentMethod);
        $("#str_all_type").val(strAllType);
        $("#str_all_amount").val(strAllAmount);
        $("#str_all_date").val(strAllDate);

    }


    me.onClickEmployeeNonFixedAllowanceDelete = function (index) {
        let deletedIndex = parseInt(index);

        CheckObj = me.Employee_OBJ;

        me.selItemCount = 1;
        $("#add_row_for_nonfixed_allowance").html("");

        me.Employee_OBJ = [];
        for (var p = 0; p < CheckObj.length; p++) {
            if (CheckObj[p].sl !== deletedIndex) {

                $("#add_row_for_nonfixed_allowance").append('<tr class="align-middle">' + '<th scope="row" class="xsm-text text-capitalize align-middle text-center">' + me.selItemCount + '</th>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="hidden" id="employee_code' + me.selItemCount + '" name="employee_code[]" value="' + CheckObj[p].employee_code + '">' + '<div id="employee_name_' + me.selItemCount + '">' + CheckObj[p].employee_name + '</div>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_fixed_all_type_' + me.selItemCount + '" class="form-control" name="cmd_fixed_all_type[]"  onchange=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")>' + '<option value="">Select Allowance Type</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<select id="cmd_payment_method_' + me.selItemCount + '" class="form-control" name="cmd_payment_method[]" onchange=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")>' + '<option value="NA">Select Payment Method</option>' + '</select>' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="number" id="all_amount_' + me.selItemCount + '" name="all_amount[]" placeholder="Enter Allowance Amount" class="form-control text-center" value="' + CheckObj[p].all_amount + '" oninput=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + '<input type="text" id="all_date_' + me.selItemCount + '" name="all_date[]" placeholder="Enter Allowance Date" class="form-control text-center" value="' + CheckObj[p].all_date + '" oninput=HRMModelJS.OnChangeValues_NonFixedAllowance("' + me.selItemCount + '")> ' + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + "<span class='text-danger d-flex align-items-center justify-content-center cursor-pointer' " + "onclick=HRMModelJS.onClickEmployeeNonFixedAllowanceDelete('" + me.selItemCount + "')><i class='fa fa-trash'></i></span>" + '</td>' + '</tr>');


                $("#cmd_fixed_all_type_" + me.selItemCount).select2();
                $("#cmd_payment_method_" + me.selItemCount).select2();
                flatpickr("#all_date_" + me.selItemCount, {});
                HRMModelJS.FillCmdNonFixedAllowanceTypeName("cmd_fixed_all_type_" + me.selItemCount, CheckObj[p].all_type);
                HRMModelJS.FillCmdEmployeePaymentMethodList("cmd_payment_method_" + me.selItemCount, CheckObj[p].employee_code, CheckObj[p].payment_method);

                me.Employee_OBJ.push({
                    sl: me.selItemCount,
                    employee_code: CheckObj[p].employee_code,
                    employee_name: CheckObj[p].employee_name,
                    all_type: CheckObj[p].all_type,
                    payment_method: CheckObj[p].payment_method,
                    all_amount: CheckObj[p].all_amount,
                    all_date: CheckObj[p].all_date
                });

                me.selItemCount++
            } // CONDITION END
        } // LOOP END

        me.SingleItem_BoxNonFixedAllowance();

    }
    //MULTIPLE NON FIXED ALLOWANCE(END)


    me.ShowBox_ForSalaryHistory = function (employee_code) {

        let formdata = new FormData();
        formdata.append('employee_code', employee_code);

        var paramas = {
            url: salary_history_detail,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };

        callAJAX(paramas, function (data) {

            $("#effect-modal-header").empty();
            $("#effect-modal-header").append('<h6 class="modal-title text-capitalize" id="set_title">Salary History</h6>' + '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' + '<span aria-hidden="true">×</span></button>');

            $("#effect-modal-body").html("");
            var container_body = $("#effect-modal-body");
            container_body.append('<div class="mb-3"> ' + '<table class="table table-bordered table-hover">' + '<thead>' + '<tr>' + '<th scope="col" class="sm-text align-middle text-center border-1 border">S/L</th>' + '<th scope="col" class="sm-text align-middle text-center border-1 border">Pay Frequency</th>' + '<th scope="col" class="sm-text align-middle text-center border-1 border">Rate Type</th>' + '<th scope="col" class="sm-text align-middle text-center border-1 border">Rate Amount</th>' + '<th scope="col" class="sm-text align-middle text-center border-1 border">Salary</th>' + '</tr>' + '</thead>' + '<tbody id="tbody_salary_history"></tbody>' + '</table>' + '</div>');

            $("#effect-modal-footer").html("");

            $('#effectModal').modal('show');

            if (data.salary_history.length > 0) {
                var count = 1;
                for (var i = 0; i < data.salary_history.length; i++) {
                    $("#tbody_salary_history").append('<tr class="xsm-text align-middle text-center">' + '<td class="xsm-text text-capitalize align-middle text-center">' + count + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.salary_history[i].pay_frequency + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.salary_history[i].rate_type + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.salary_history[i].rate_amount + '</td>' + '<td class="xsm-text text-capitalize align-middle text-center">' + data.salary_history[i].basic_salary + '</td>' + '</tr>');
                    count++;
                }

            } else {
                $("#tbody_salary_history").append('<tr><td class="xsm-text text-capitalize align-middle text-center" colspan="5">NO HISTORY FOUND</td></tr>');
            }
        });
    }

// PAYROLL PAY SALARY FUNCTION
    me.MakePayrollPayments = function () {
        var payroll_code = [];
        $('input:checkbox[name=employee_code]:checked').each(function () {
            payroll_code.push($(this).val());
        });

        var strEmployeeArray = "";
        if (payroll_code.length === 0) {
            strEmployeeArray = "'99999'";
        }
        if (payroll_code.length === 1) {
            strEmployeeArray = "'" + payroll_code[0] + "'";
        }
        if (payroll_code.length > 1) {
            var count = 1;
            strEmployeeArray = "";
            for (let i = 0; i <= payroll_code.length; i++) {
                if (count === 1) {
                    strEmployeeArray += "'" + payroll_code[i] + "', ";
                }
                if (count > 1 && count < payroll_code.length) {
                    strEmployeeArray = strEmployeeArray + "'" + payroll_code[i] + "', ";
                }
                if (count === payroll_code.length) {
                    strEmployeeArray = strEmployeeArray + "'" + payroll_code[i] + "'";
                }
                count++
            }
        }

        let formdata = new FormData();
        formdata.append('payroll_code', strEmployeeArray);

        var paramas = {
            url: make_payroll_payments,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            // console.log(data.message);
            if (data.message === "Success") {
                location.reload();
            }
        });

    }

    ////DELETED EMPLOYEE FORMAT
//     me.DeleteEmployeeFormatdata = function () {
//
//         var paramas = {
//             url: delete_emp_format,
//             type: "POST",
//             dataType: 'json',
//             headers: {'X-CSRFToken': posttoken}
//         };
//         callAJAX(paramas, function (data) {
//             // alert(data.message);
//
//             if (data.message === "Success") {
//                 // location.reload();
//                 location.reload();
//             }
//         });
//
// }
//     me.GetPositionOnFromLocation = function (cmd_id, selected_value) {
//         var store_location = $("#store_location").val();
//
//         let formdata = new FormData();
//         formdata.append('store_location', store_location);
//
//         var paramas = {
//             url: get_employee_position_from_location,
//             data: formdata,
//             type: "POST",
//             dataType: 'json',
//             headers: {'X-CSRFToken': posttoken}
//         };
//         callAJAX(paramas, function (data) {
//
//                if (data.cmd_list.length > 0) {
//                 var sbox = document.getElementById(cmd_id);
//                 $("#" + cmd_id).empty();
//
//                 $("#" + cmd_id).append("<option value='%'>Choose One</option>");
//                 $("#" + cmd_id + "> option").removeAttr("selected");
//                 for (var i = 0; i < data.cmd_list.length; i++) {
//                 sbox.add(new Option(data.cmd_list[i]["position_name"], data.cmd_list[i]["position_code"]));
//                 }
//                 if (selected_value !== "") {
//                     $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
//                     $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
//                 }
//             } else {
//                 $("#" + cmd_id + "> option").removeAttr("selected");
//                 $('#' + cmd_id).empty();
//                 $('#' + cmd_id).append("<option value=''>No Record Found</option>");
//             }
//         });
//     }
//

    me.GetEmployeeFromPosition_and_Location = function (cmd_id,selected_value) {

        var cmd_designation = $("#cmd_designation").val();
        var store_location = $("#store_location").val();

        let formdata = new FormData();
        formdata.append('cmd_designation', cmd_designation);
        formdata.append('store_location', store_location);

        var paramas = {
            url: get_employee_name_from_position_and_location,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };

        callAJAX(paramas, function (data) {

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value='NA'>Choose One</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i]["title"], data.cmd_list[i]["employee_code"]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            } else {
                $("#" + cmd_id + "> option").removeAttr("selected");
                $('#' + cmd_id).empty();
                $('#' + cmd_id).append("<option value=''>No Record Found</option>");
            }
        });
    }


}