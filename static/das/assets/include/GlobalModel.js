AppGlobalModel = function () {

    var me = this;

    me.appConstructor = function () {
    };

    me.FillCmdListByModel = function (table_name, column_name, column_code, cmd_id, selected_value) {
        let formdata = new FormData();
        formdata.append('table_name', table_name);
        formdata.append('column_name', column_name);
        formdata.append('column_code', column_code);
        var paramas = {
            url: cmd_list_model,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.cmd_list.length; i++) {
                sbox.add(new Option(data.cmd_list[i][column_name], data.cmd_list[i][column_code]));
                // $('#' + cmd_id + ' option[value="' + data.cmd_list[i][column_code] + '"]').prop('disabled', true);
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }
        });

    };

    me.FillCmdListByModelWithCode = function (table_name, condition_column, cmd_column, cmd_id, selected_value) {
        let formdata = new FormData();
        formdata.append('table_name', table_name);
        formdata.append('condition_column', condition_column);
        formdata.append('cmd_column', cmd_column);
        var paramas = {
            url: fill_cmd_model_with_code,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            let column_split = cmd_column.split("^^")
            let column_code = column_split[0]
            let column_name = column_split[1]

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value='NA'>Select</option>");
                $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i][column_name], data.cmd_list[i][column_code]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            } else {
                $("#" + cmd_id + "> option").removeAttr("selected");
                // $("#" + cmd_id).trigger("change");
                $('#' + cmd_id).empty();
                $('#' + cmd_id).append("<option value=''>No Record Found</option>");
            }
        })
    };

    me.FetchMaterialItemList = function (table_name, column_name, column_code, cmd_id, selected_value) {
        let formdata = new FormData();
        formdata.append('table_name', table_name);
        formdata.append('column_name', column_name);
        formdata.append('column_code', column_code);
        var paramas = {
            url: cmd_list_model,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            // console.log(data);
            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.cmd_list.length; i++) {
                sbox.add(new Option(data.cmd_list[i]["material_code"] + ", " + data.cmd_list[i]["material_name"], data.cmd_list[i]["material_code"]));
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }
        });
    }

    me.FillCmdListByModelWithNameAndCode = function (table_name, condition_column, cmd_column, cmd_id, selected_value) {
        let formdata = new FormData();
        formdata.append('table_name', table_name);
        formdata.append('condition_column', condition_column);
        formdata.append('cmd_column', cmd_column);
        var paramas = {
            url: fill_cmd_model_with_code,
            data: formdata,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            let column_split = cmd_column.split("^^")
            let column_code = column_split[0]
            let column_name = column_split[1]

            $('#' + cmd_id).empty("");
            $('#' + cmd_id).append("<option value='NA'>Select</option>");
            $("#" + cmd_id + "> option").removeAttr("selected");
            $("#" + cmd_id).trigger("change");

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i][column_name] + ' ,  ' + data.cmd_list[i][column_code], data.cmd_list[i][column_code]));
                }
                if (selected_value !== "") {
                    $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                    $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
                }
            }
        })
    };

    //// CHART OF ACCOUNT START

    me.CmdCOAChildList = function (cmd_id, selected_value) {
        var paramas = {
            url: cmd_coa_child,
            type: "POST",
            dataType: 'json',
            headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {
            // console.log(data);
            var sbox = document.getElementById(cmd_id);
            for (var i = 0; i < data.cmd_list.length; i++) {
                sbox.add(new Option(data.cmd_list[i]["child_name"], data.cmd_list[i]["child_code"]));
            }
            if (selected_value !== "") {
                $("#" + cmd_id).val(selected_value); // Select the option with a value of '1'
                $("#" + cmd_id).trigger('change'); // Notify any JS components that the value changed
            }
        });
    };
    //// CHART OF ACCOUNT END

    //// GLOBAL FUNCTION
    me.ExportToExcel = function (table_id, sheet_name, type, fn, dl) {
        var elt = document.getElementById(table_id);  /////  give id to the table "Import_excel"
        var wb = XLSX.utils.table_to_book(elt, {sheet: sheet_name});
        return dl ?
            XLSX.write(wb, {bookType: type, bookSST: true, type: 'base64'}) :
            XLSX.writeFile(wb, fn || (sheet_name + (type || '.xlsx')));
    }
// THIS FUNCTION HAVE BEEN USED TO GET THE LATEST CHILD CODE AGAINST SUB PARENT
    me.GetLatestChildCode = function () {
        var get_sub_parent_code = $('#cmd_sub_parent').val();

        // NULL LATEST CHILD CODE WHEN PARENT IS CHANGED
        $("#cmd_parent").change(function () {
            $('#child_code').val(null);
        });
        // NULL LATEST CHILD CODE WHEN SUB PARENT IS CHANGED
        if (get_sub_parent_code === 'NA') {
            $('#child_code').val(null);

        } else {
            let formdata = new FormData();
            formdata.append('get_sub_parent_code', get_sub_parent_code);
            var paramas = {
                url: latest_child_code,
                data: formdata,
                type: "POST",
                dataType: 'json',
                headers: {'X-CSRFToken': posttoken}
            };
            callAJAX(paramas, function (data) {
                // alert(data.new_code)
                var new_code = data.new_code;
                $('#child_code').val(new_code);
            });
        }


    }

    //SHOW All Country Name
    me.GetAllCountry = function (cmd_id, selected_value) {
        var paramas = {
            url: get_all_country, type: "POST", dataType: 'json', headers: {'X-CSRFToken': posttoken}
        };
        callAJAX(paramas, function (data) {

            if (data.cmd_list.length > 0) {
                var sbox = document.getElementById(cmd_id);
                $("#" + cmd_id).empty();

                $("#" + cmd_id).append("<option value='NA'>Select</option>");
                // $("#" + cmd_id + "> option").removeAttr("selected");
                for (var i = 0; i < data.cmd_list.length; i++) {
                    sbox.add(new Option(data.cmd_list[i]["country_name"], data.cmd_list[i]["country_code"]));
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

setMissingParams = function (params, isAsync) {
    if (!params["type"]) {
        params["type"] = "GET";
    }
    if (!params["dataType"]) {
        params["dataType"] = "json";
    }
    if (!params["processData"]) {
        params["processData"] = false;
    }
    if (!params["contentType"]) {
        params["contentType"] = false;
    }

    if (!params["async"]) {
        params["async"] = isAsync;
    }
    return params;
}

callAJAX = function (params, callback) {
    // params in the form of {url:url,post:post} ets
    var params = setMissingParams(params, true);
    // if ($("#waiting-div").length) $("#waiting-div").css('visibility', 'visible');
    var delayInMilliseconds = 1000; //1 second
    setTimeout(function () {
        $.ajax(params).done(function (data) {
            // if ($("#waiting-div").length) $("#waiting-div").css('visibility', 'hidden');
            try {
                if (data.is_redirect) {
                    window.location.href = data.url
                }
            } catch (e) {
                console.log(e)
            }
            callback(data)
        }).fail(function (error, texStatus) {
            // console.log(error.responseText);
            // if ($("#waiting-div").length) $("#waiting-div").css('visibility', 'hidden');
            console.log(texStatus)
            errorMsg = "Fail to perform your request."
            // showAlertDialog(errorMsg, dialogTypes.error);
            // if (progressbarModel != null)
            //     progressbarModel.hideProgressBar()
        })
            , delayInMilliseconds
    })
}

window.successAvatarBox = function (show_id, msg) {
    var dom = '<div class="alert style-1 alert-success alert-dismissible fade show" role="alert">' +
        '<p class="mb-0 alert_content"><span class="avatar avatar-sm bg-success radius-4 me-2"><i class="fas fa-check-circle text-white"></i></span>' +
        'Success! ' + msg + '</p><button aria-label="Close" class="btn-close" data-bs-dismiss="alert" type="button"><span aria-hidden="true">×</span>' +
        '</button></div>';
    var jdom = $(dom);
    jdom.hide();
    $("#" + show_id).append(jdom);
    jdom.fadeIn();
    setTimeout(function () {
        jdom.fadeOut(function () {
            jdom.remove();
        });
    }, 3000);
}

window.errorAvatarBox = function (show_id, msg) {
    var dom = '<div class="alert style-1 alert-secondary alert-dismissible fade show" role="alert">' +
        '<p class="mb-0 alert_content"><span class="avatar avatar-sm bg-secondary radius-4 me-2"><i class="fas fa-check-circle text-white"></i></span>' +
        'Error! ' + msg + '</p><button aria-label="Close" class="btn-close" data-bs-dismiss="alert" type="button"><span aria-hidden="true">×</span>' +
        '</button></div>';
    var jdom = $(dom);
    jdom.hide();
    $("#" + show_id).append(jdom);
    jdom.fadeIn();
    setTimeout(function () {
        jdom.fadeOut(function () {
            jdom.remove();
        });
    }, 3000);
}

////SWEET ALERT BOOTSNIPP
window.error = function (directions, msg) {
    var dom = '<div id="toast-container" class="' + directions + '">' +
        '<div class="toast-error" aria-live="assertive" style="">' +
        ' <button type="button" class="toast-close-button" role="button">×</button>' +
        '<div class="toast-title">Warning!</div><div class="toast-message"><div><p>' + msg + '</p></div></div></div></div>';
    var jdom = $(dom);
    jdom.hide();
    $("body").append(jdom);
    jdom.fadeIn();
    setTimeout(function () {
        jdom.fadeOut(function () {
            jdom.remove();
        });
    }, 4000);
}
window.warning = function (directions, msg) {
    var dom = '<div id="toast-container" class="' + directions + '"><div class="toast-warning" aria-live="assertive" style=""> <button type="button" class="toast-close-button" role="button">×</button><div class="toast-title">Warning!</div><div class="toast-message"><div><p>' + msg + '</p></div></div></div></div>';
    var jdom = $(dom);
    jdom.hide();
    $("body").append(jdom);
    jdom.fadeIn();
    setTimeout(function () {
        jdom.fadeOut(function () {
            jdom.remove();
        });
    }, 4000);
}
window.info = function (directions, msg) {
    var dom = '<div id="toast-container" class="' + directions + '"><div class="toast-info" aria-live="assertive" style=""> <button type="button" class="toast-close-button" role="button">×</button><div class="toast-title">Info!</div><div class="toast-message"><div><p>' + msg + '</p></div></div></div></div>';
    var jdom = $(dom);
    jdom.hide();
    $("body").append(jdom);
    jdom.fadeIn();
    setTimeout(function () {
        jdom.fadeOut(function () {
            jdom.remove();
        });
    }, 4000);
}
window.success = function (directions, msg) {
    var dom = '<div id="toast-container" class="' + directions + '"><div class="toast-success" aria-live="polite" style=""><button type="button" class="toast-close-button" role="button">×</button><div class="toast-title">Success!</div><div class="toast-message">' + msg + '</div></div></div>';
    var jdom = $(dom);
    jdom.hide();
    $("body").append(jdom);
    jdom.fadeIn();
    setTimeout(function () {
        jdom.fadeOut(function () {
            jdom.remove();
        });
    }, 4000);
}
