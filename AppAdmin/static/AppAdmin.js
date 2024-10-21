AppAdminModel = function () {

    let me = this;
    me.appConstructor = function () {
    }

    me.ShowBox_AddPayment = function (param) {
        var split = param.split(",");

        var action_type = split[0];
        var pm_code = "";
        var pm_name = "";
        if (action_type === "UPDATE") {
            pm_code = split[1];
            pm_name = split[2];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_payment_method"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='pm_code' name='pm_code' value='" + pm_code + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Payment Method Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="pm_name" name="pm_name" ' +
            "placeholder='e.g. Cash, Jazz Cash, Easy Paisa, Bank' value='" + pm_name + "'></div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdminModelJS.AddPayment();" class="btn btn-sm w-50 btn-success" type="button">Save</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_payment_method").html("Add Payment Method");
        if (split[0] === "UPDATE") {
            $("#pm_name").val(split[2]);
            $("#title_payment_method").html("Update Payment Method");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    // line business code start
    me.ShowBox_LineBussiness = function (param) {
        // alert(param);

        var split = param.split("^^");
        var action_type = split[0];
        var line_buss_code = "";
        var line_buss_name = "";
        var get_id = "";
        if (action_type === "UPDATE") {
            line_buss_code = split[1];
            line_buss_name = split[2];
            get_id = split[3];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='get_id' name='get_id' value='" + get_id + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Line of Bussiness Code: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="line_buss_code" name="line_buss_code" ' +
            "placeholder='e.g. 01, 02, 03 ' value='" + line_buss_code + "'>" +
            '<label for="recipient-name" class="col-form-label">Line of Bussiness Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="line_buss_name" name="line_buss_name" ' +
            "placeholder='Enter Line of Bussiness Name' value='" + line_buss_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.LineBussiness();" class="btn btn-sm w-50 btn-success" type="button">Save Line Bussiness</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title").html("Add new  Line Bussiness");
        if (split[0] === "UPDATE") {
            $("#line_buss_code").val(split[1]);
            $("#line_buss_name").val(split[2]);
            $("#title_emp_department").html("update  Line Bussiness");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.LineBussiness = function () {
        var action_type = $("#action_type").val();
        var line_buss_code = $("#line_buss_code").val();
        var line_buss_name = $("#line_buss_name").val();
        var get_id = $("#get_id").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('line_buss_code', line_buss_code);
        formdata.append('line_buss_name', line_buss_name);
        formdata.append('get_id', get_id);

        swal({
                title: "Line of Bussiness",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_line_bussiess,
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
    // line business code end

    me.DeleteLineBussiness = function (id) {
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
            },
            function (isConfirm) {
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
                            swal("Deleted!", "Your Line of Business has been deleted.", "success");
                            if (data.message === "Success") {
                                location.reload();
                            }
                        }
                    );

                } else {
                    swal("Cancelled", "Your Line of Business is safe :)", "error");
                }
            });
    }

    // BusinessSector code start
    me.ShowBox_BussinessSector = function (param) {
        // alert(param);

        var split = param.split("^^");
        var action_type = split[0];
        var buss_sect_code = "";
        var buss_sect_name = "";
        var get_id = "";
        if (action_type === "UPDATE") {
            buss_sect_code = split[1];
            buss_sect_name = split[2];
            get_id = split[3];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='get_id' name='get_id' value='" + get_id + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Bussiness Sector Code: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="buss_sect_code" name="buss_sect_code" ' +
            "placeholder='e.g 01, 02, 03 ' value='" + buss_sect_code + "'>" +

            '<label for="recipient-name" class="col-form-label">Bussiness Sector Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="buss_sect_name" name="buss_sect_name" ' +
            "placeholder='Enter Business Sector Name ' value='" + buss_sect_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.BussinessSector();" class="btn btn-sm w-50 btn-success" type="button">Save Bussiness Sector</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title").html("Add new Bussiness Sector");
        if (split[0] === "UPDATE") {
            $("#buss_sect_code").val(split[1]);
            $("#buss_sect_name").val(split[2]);
            $("#get_id").val(split[3]);
            $("#title_emp_department").html("update Bussiness Sector");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.BussinessSector = function () {
        var action_type = $("#action_type").val();
        var buss_sect_code = $("#buss_sect_code").val();
        var buss_sect_name = $("#buss_sect_name").val();
        var get_id = $("#get_id").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('buss_sect_code', buss_sect_code);
        formdata.append('buss_sect_name', buss_sect_name);
        formdata.append('get_id', get_id);

        swal({
                title: "Bussiness Sector",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_bussiness_sector,
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
    // BusinessSector code end

    me.DeleteBussinessSector = function (id) {
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
            },
            function (isConfirm) {
                if (isConfirm) {

                    let formdata = new FormData();
                    formdata.append('id', id);
                    var paramas = {
                        url: delete_single_bussiness_sector,
                        data: formdata,
                        type: "POST",
                        dataType: 'json',
                        headers: {'X-CSRFToken': posttoken}
                    };
                    callAJAX(paramas, function (data) {
                            // console.log(data.PV_List);
                            swal("Deleted!", "Your Business Sector has been deleted.", "success");
                            if (data.message === "Success") {
                                location.reload();
                            }
                        }
                    );

                } else {
                    swal("Cancelled", "Your Business Sector is safe :)", "error");
                }
            });
    }

    // Cost Center code start
    me.ShowBox_CostCenter = function (param) {
        // alert(param);

        var split = param.split("^^");
        var action_type = split[0];
        var cost_center_code = "";
        var cost_center_name = "";
        if (action_type === "UPDATE") {
            cost_center_code = split[1];
            cost_center_name = split[2];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='cost_center_code' name='cost_center_code' value='" + cost_center_code + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Cost Center Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="cost_center_name" name="cost_center_name" ' +
            "placeholder='Enter Cost Center Name' value='" + cost_center_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.CostCenter();" class="btn btn-sm w-50 btn-success" type="button">Save Cost Senter</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title").html("Add new  Cost Center");
        if (split[0] === "UPDATE") {
            $("#cost_center_name").val(split[2]);
            $("#title_emp_department").html("update  Cost Center");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.CostCenter = function () {
        var action_type = $("#action_type").val();
        var cost_center_code = $("#cost_center_code").val();
        var cost_center_name = $("#cost_center_name").val();


        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('cost_center_code', cost_center_code);
        formdata.append('cost_center_name', cost_center_name);


        swal({
                title: "Cost Center",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_cost_center,
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
    // Cost Center code end

    // Cost Location Data start
    me.ShowBox_LocationData = function (param) {
        // alert(param);

        var split = param.split("^^");
        var action_type = split[0];
        var loc_code = "";
        var loc_name = "";

        if (action_type === "UPDATE") {
            loc_code = split[1];
            loc_name = split[2];

        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='loc_code' name='loc_code' value='" + loc_code + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Location Data Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="loc_name" name="loc_name" ' +
            "placeholder='Enter Location Data Name' value='" + loc_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.LocationData();" class="btn btn-sm w-50 btn-success" type="button">Save Location Data</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title").html("Add new  Location Data");
        if (split[0] === "UPDATE") {
            $("#loc_code").val(split[1]);
            $("#loc_name").val(split[2]);
            $("#title_emp_department").html("update  Location Data");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.LocationData = function () {
        var action_type = $("#action_type").val();
        var loc_code = $("#loc_code").val();
        var loc_name = $("#loc_name").val();


        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('loc_code', loc_code);
        formdata.append('loc_name', loc_name);


        swal({
                title: "Location Data",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_location_data,
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
    // Cost Location Data end

    // Cost Location City start
    me.ShowBox_LocationCity = function (param) {
        // alert(param);

        var split = param.split("^^");
        var action_type = split[0];
        var city_code = "";
        var city_name = "";

        if (action_type === "UPDATE") {
            city_code = split[1];
            city_name = split[2];

        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='city_code' name='city_code' value='" + city_code + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Location City Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="city_name" name="city_name" ' +
            "placeholder='Enter Location City Name' value='" + city_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.LocationCity();" class="btn btn-sm w-50 btn-success" type="button">Save Location City</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title").html("Add new  Location City");
        if (split[0] === "UPDATE") {
            $("#city_code").val(split[1]);
            $("#city_name").val(split[2]);
            $("#title_emp_department").html("update  Location City");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.LocationCity = function () {
        var action_type = $("#action_type").val();
        var city_code = $("#city_code").val();
        var city_name = $("#city_name").val();


        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('city_code', city_code);
        formdata.append('city_name', city_name);


        swal({
                title: "Location City",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_location_city,
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
    // Cost Location City end
    me.ShowLocationStoreCombineCode = function () {
        var get_location_city = $('#cmd_location_city').val();
        var get_location_data = $('#cmd_location_data').val();

        if (get_location_data !== "" && get_location_city !== "") {
            let formdata = new FormData();
            formdata.append('get_location_city', get_location_city);
            formdata.append('get_location_data', get_location_data);
            var paramas = {
                url: unique_location_store_code,
                data: formdata,
                type: "POST",
                dataType: 'json',
                headers: {'X-CSRFToken': posttoken}
            };
            callAJAX(paramas, function (data) {
                var selectedValue = data.combine_code;
                $('#id_loc_store_code').val(selectedValue);
            });
        } else {
        }
    }


    //// SEGMENT END

    ////ADDED NEW EMPLOYEE POSITION
    me.AddPayment = function () {
        var action_type = $("#action_type").val();
        var pm_code = $("#pm_code").val();
        var pm_name = $("#pm_name").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('pm_code', pm_code);
        formdata.append('pm_name', pm_name);

        swal({
                title: "Payment Method",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_payment_method,
                        data: formdata,
                        type: "POST",
                        dataType: 'json',
                        headers: {'X-CSRFToken': posttoken}
                    };
                    callAJAX(paramas, function (data) {
                        // console.log(data.message);
                        if (data.message === "Success") {
                            swal("Successfully!", "Payment Method has been Created.", "success");
                            location.reload();
                        }
                        if (data.message === "Update") {
                            swal("Successfully!", "Payment Method has been Updated.", "success");
                            location.reload();
                        }
                    });
                } else {
                    swal("Cancelled", "Please Re-check your Status :)", "error");
                }
            });
    }

    me.DeletePaymentView = function (id) {

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

            },
            function (isConfirm) {
                if (isConfirm) {

                    let formdata = new FormData();
                    formdata.append('id', id);
                    var paramas = {
                        url: delete_single_payment_item,
                        data: formdata,
                        type: "POST",
                        dataType: 'json',
                        headers: {'X-CSRFToken': posttoken}
                    };
                    callAJAX(paramas, function (data) {
                            // console.log(data.PV_List);
                            swal("Deleted!", "Your Payment Method has been deleted.", "success");
                            if (data.message === "Success") {
                                location.reload();
                            }
                        }
                    );

                } else {
                    swal("Cancelled", "Your Payment Method is safe :)", "error");
                }
            });
    }
    //// PAYMENT METHOD END

    //// BANK LIST START
    me.ShowBox_AddNewBank = function (param) {
        var split = param.split(",");

        var action_type = split[0];
        var bank_id = "";
        var bank_code = "";
        var bank_name = "";
        if (action_type === "UPDATE") {
            bank_id = split[1];
            bank_code = split[2];
            bank_name = split[3];
        }

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");

        container.append('<h6 class="modal-title text-capitalize" id="title_Bank_Data"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');

        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            "<input type='hidden' id='action_type' name='action_type' value='" + action_type + "' autocomplete='off'>" +
            "<input type='hidden' id='bank_id' name='bank_id' value='" + bank_id + "' autocomplete='off'>" +
            '<label for="recipient-name" class="col-form-label">Bank Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="bank_name" name="bank_name" ' +
            "placeholder='e.g. Allied Bank, United Bank Limited' value='" + bank_name + "'>" +
            '<label for="recipient-name" class="col-form-label">Bank Code: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="bank_code" name="bank_code" ' +
            "placeholder='e.g. ABL, UBL ' value='" + bank_code + "'></div>");


        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdminModelJS.AddNewBank();" class="btn btn-sm w-50 btn-success" type="button">Save</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        $("#title_Bank_Data").html("Add Bank Data");
        if (split[0] === "UPDATE") {
            $("#bank_id").val(split[1]);
            $("#bank_name").val(split[2]);
            $("#bank_code").val(split[3]);

            $("#title_Bank_Data").html("Update Bank Data");
        }

        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');

    }

    me.AddNewBank = function () {
        var action_type = $("#action_type").val()
        var bank_id = $("#bank_id").val();
        var bank_code = $("#bank_code").val();
        var bank_name = $("#bank_name").val();

        let formdata = new FormData();
        formdata.append('action_type', action_type);
        formdata.append('bank_id', bank_id);
        formdata.append('bank_name', bank_name);
        formdata.append('bank_code', bank_code);

        swal({
                title: "Bank",
                text: action_type,
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_new_bank_list,
                        data: formdata,
                        type: "POST",
                        dataType: 'json',
                        headers: {'X-CSRFToken': posttoken}
                    };
                    callAJAX(paramas, function (data) {
                        // console.log(data.message);
                        if (data.message === "Success") {
                            swal("Successfully!", "New Bank has been Created.", "success");
                            location.reload();
                        }
                        if (data.message === "Update") {
                            swal("Successfully!", "Bank has been Updated.", "success");
                            location.reload();
                        }
                    });
                } else {
                    swal("Cancelled", "Please Re-check your Status :)", "error");
                }
            });
    }

    me.DeleteBankView = function (id) {
        swal({
                title: "Are you sure?",
                text: "You will not be able to recover theses bank details!",
                type: "warning",
                showCancelButton: true,
                confirmButtonClass: "btn-danger",
                confirmButtonText: "Yes, Delete it!",
                cancelButtonText: "No, Cancel!",
                closeOnConfirm: false,
                closeOnCancel: false

            },
            function (isConfirm) {
                if (isConfirm) {

                    let formdata = new FormData();
                    formdata.append('id', id);
                    var paramas = {
                        url: delete_bank_list,
                        data: formdata,
                        type: "POST",
                        dataType: 'json',
                        headers: {'X-CSRFToken': posttoken}
                    };
                    callAJAX(paramas, function (data) {
                            // console.log(data.PV_List);
                            swal("Deleted!", "Your Bank has been deleted.", "success");
                            if (data.message === "Success") {
                                location.reload();
                            }
                        }
                    );

                } else {
                    swal("Cancelled", "Your Bank are safe :)", "error");
                }
            });
    }
    //// BANK LIST END

    ///// GEO HIERARCHY STARTS
    me.ShowBox_AddNewCountry = function () {


        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');
        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +

            '<select name="cmd_country" class="form-control form-select select2" id="cmd_country">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.AddCountry();" class="btn btn-sm w-50 btn-success" type="button">Save Country</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');
        AdmineModelJS.GetAllCountryFromJson("cmd_country", "");

        $('#cmd_country').select2({
            dropdownParent: $('#effectModal')
        });

        $("#title").html("Add new Country");
        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddCountry = function () {
        var cmd_country = $("#cmd_country").val();


        let formdata = new FormData();
        formdata.append('cmd_country', cmd_country);
        swal({
                title: "Country Data",
                text: 'NEW',
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_new_country,
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
                } else {
                    swal("Cancelled", "Please Re-check your Status :)", "error");
                }
            });
    }

    //SHOW All Country Name From Json
    me.GetAllCountryFromJson = function (cmd_id, selected_value) {
        var paramas = {
            url: get_all_country_from_json, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value=''>Select</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option('(' + data.cmd_list[i]["code"] + ')' + '-' + data.cmd_list[i]["country"] , data.cmd_list[i]["iso"] + '^' +data.cmd_list[i]["code"] + '^' + data.cmd_list[i]["country"]));
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

    me.ShowBox_AddNewState = function () {

        var state_name = "";

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');
        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            '<label for="recipient-name" class="col-form-label">Country Name: <small class="text-warning">*</small></label>' +
            '<select name="cmd_country" class="form-control form-select select2" id="cmd_country">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            '<label for="recipient-name" class="col-form-label">State Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="state_name" name="state_name" ' +
            "placeholder='Enter State Name' value='" + state_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.AddState();" class="btn btn-sm w-50 btn-success" type="button">Save State</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        GlobalModelJS.GetAllCountry("cmd_country", "");
        $("#cmd_country").select2();

        $("#title").html("Add new State");
        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddState = function () {
        var state_name = $("#state_name").val();
        var cmd_country = $("#cmd_country").val();

        let formdata = new FormData();
        formdata.append('state_name', state_name);
        formdata.append('cmd_country', cmd_country);

        swal({
                title: "State Data",
                text: 'NEW',
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_new_state,
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
                } else {
                    swal("Cancelled", "Please Re-check your Status :)", "error");
                }
            });
    }


    me.ShowBox_AddNewCity = function () {

        var city_name = "";

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');
        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            '<label for="recipient-name" class="col-form-label">Country: <small class="text-warning">*</small></label>' +
            '<select name="cmd_country" class="form-control form-select select2" id="cmd_country">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            '<label for="recipient-name" class="col-form-label">State: <small class="text-warning">*</small></label>' +
            '<select name="cmd_state" class="form-control form-select select2" id="cmd_state">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            '<label for="recipient-name" class="col-form-label">City Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="city_name" name="city_name" ' +
            "placeholder='Enter City Name' value='" + city_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.AddCity();" class="btn btn-sm w-50 btn-success" type="button">Save City</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        GlobalModelJS.GetAllCountry("cmd_country", "");

        $("#cmd_country").change(function (e) {
            var selected_value = e.target.value;
            let condition_column = "country_code=" + selected_value;
            let cmd_column = "state_code^^state_name";
            GlobalModelJS.FillCmdListByModelWithCode("tbl_state_data", condition_column, cmd_column, "cmd_state", "");
        });
        $("#cmd_country").select2();
        $("#cmd_state").select2();

        $("#title").html("Add new City");
        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddCity = function () {
        var city_name = $("#city_name").val();
        var cmd_state = $("#cmd_state").val();

        let formdata = new FormData();
        formdata.append('city_name', city_name);
        formdata.append('cmd_state', cmd_state);

        swal({
                title: "City Data",
                text: 'NEW',
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_new_city,
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
                } else {
                    swal("Cancelled", "Please Re-check your Status :)", "error");
                }
            });
    }

    me.ShowBox_AddNewArea = function () {

        var area_name = "";

        $("#effect-modal-header").empty();
        var container = $("#effect-modal-header");
        container.append('<h6 class="modal-title text-capitalize" id="title"></h6>' +
            '<button aria-label="Close" class="btn-close" data-bs-dismiss="modal" type="button">' +
            '<span aria-hidden="true">×</span></button>');
        $("#effect-modal-body").html("");
        var container_body = $("#effect-modal-body");
        container_body.append('<div class="mb-3">' +
            '<label for="recipient-name" class="col-form-label">Country: <small class="text-warning">*</small></label>' +
            '<select name="cmd_country" class="form-control form-select select2" id="cmd_country">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            '<label for="recipient-name" class="col-form-label">State: <small class="text-warning">*</small></label>' +
            '<select name="cmd_state" class="form-control form-select select2" id="cmd_state">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            '<label for="recipient-name" class="col-form-label">City: <small class="text-warning">*</small></label>' +
            '<select name="cmd_city" class="form-control form-select select2" id="cmd_city">' +
            '<option value="NA">Select</option>' +
            '</select>' +
            '<label for="recipient-name" class="col-form-label">Area Name: <small class="text-warning">*</small></label>' +
            '<input type="text" class="form-control" id="area_name" name="area_name" ' +
            "placeholder='Enter Area Name' value='" + area_name + "'>" +
            "</div>");

        $("#effect-modal-footer").html("");
        var container_footer = $("#effect-modal-footer");
        container_footer.append('<button onclick="AdmineModelJS.AddArea();" class="btn btn-sm w-50 btn-success" type="button">Save Area</button>' +
            '<button class="btn btn-sm w-25 btn-danger" data-bs-dismiss="modal" type="button">Close</button>');

        GlobalModelJS.GetAllCountry("cmd_country", "");

        $("#cmd_country").change(function (e) {
            $("#cmd_city").empty();
            $("#cmd_city").append("<option value='NA'>Select</option>");

            var selected_value = e.target.value;
            let condition_column = "country_code=" + selected_value;
            let cmd_column = "state_code^^state_name";
            GlobalModelJS.FillCmdListByModelWithCode("tbl_state_data", condition_column, cmd_column, "cmd_state", "");
        });

        $("#cmd_state").change(function (e) {
            var selected_value = e.target.value;
            let condition_column = "state_code=" + selected_value;
            let cmd_column = "city_code^^city_name";
            GlobalModelJS.FillCmdListByModelWithCode("tbl_city_data", condition_column, cmd_column, "cmd_city", "");
        });

        $("#cmd_country").select2();
        $("#cmd_state").select2();
        $("#cmd_city").select2();

        $("#title").html("Add new City");
        $('#effectModal').addClass("effect-newspaper");
        $('#effectModal').modal('show');
    }

    me.AddArea = function () {
        var area_name = $("#area_name").val();
        var cmd_city = $("#cmd_city").val();


        let formdata = new FormData();
        formdata.append('area_name', area_name);
        formdata.append('cmd_city', cmd_city);


        swal({
                title: "Area Town",
                text: 'NEW',
                type: "success",
                showCancelButton: true,
                confirmButtonClass: "btn btn-danger",
                confirmButtonText: "Yes, Confirm!",
                closeOnConfirm: false
            },
            function (isConfirm) {
                if (isConfirm) {
                    var paramas = {
                        url: add_new_area,
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
                } else {
                    swal("Cancelled", "Please Re-check your Status :)", "error");
                }
            });
    }

    ///// GEO HIERARCHY END


}