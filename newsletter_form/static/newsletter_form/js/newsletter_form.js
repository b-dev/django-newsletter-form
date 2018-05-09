$(function () {

    // Get the modal
    var modal = document.getElementById('modalNewsletterForm');

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("modal-newsletter-form-close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // CSRF TOKEN
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function subscribe_to_newsletter() {
        var button_newsletter = $("#id_button_form_iscrizione_newsletter");
        var email_address = $("#id_email_form_iscrizione_newsletter").val();
        if (manage_first_name == true) {
            var first_name = $("#id_first_name_form_iscrizione_newsletter").val();
        }
        if (manage_first_name == true) {
            var last_name = $("#id_last_name_form_iscrizione_newsletter").val();
        }
        var terms_of_use_checked = $("#id_flag_terms_of_use").prop("checked");

        var div_errore_email_newsletter = $("#id_error_email_form_iscrizione_newsletter");
        var div_errore_first_name_newsletter = $("#id_error_first_name_form_iscrizione_newsletter");
        var div_errore_last_name_newsletter = $("#id_error_last_name_form_iscrizione_newsletter");
        var div_errore_terms_of_use_newsletter = $("#id_error_flag_terms_of_use_form_iscrizione_newsletter");

        div_errore_email_newsletter.hide();
        div_errore_first_name_newsletter.hide();
        div_errore_last_name_newsletter.hide();
        div_errore_terms_of_use_newsletter.hide();

        var ci_sono_errori = false;
        if (email_address == '') {
            div_errore_email_newsletter.show();
            ci_sono_errori = true;
        }
        if (manage_first_name == true && first_name_mandatory == true && first_name == '') {
            div_errore_first_name_newsletter.show();
            ci_sono_errori = true;
        }
        if (manage_last_name == true && last_name_mandatory == true && last_name == '') {
            div_errore_last_name_newsletter.show();
            ci_sono_errori = true;
        }
        if (terms_of_use_checked == false) {
            div_errore_terms_of_use_newsletter.show();
            ci_sono_errori = true;
        }

        if (ci_sono_errori == false) {
            button_newsletter.attr("disabled", true);
            button_newsletter.html(text_newsletter_button_disabled);
            var data = {'csrfmiddlewaretoken': csrftoken,
                        'email_newsletter': email_address}
            if (manage_first_name == true) {
                data['first_name'] = first_name;
            }
            if (manage_last_name == true) {
                data['last_name'] = last_name;
            }
            data['flag_terms_of_use'] = ''
            if(terms_of_use_checked == true) {
                data['flag_terms_of_use'] = 'on'
            }
            $.post(url_iscrizione_newsletter, data, subscribe_to_newsletter_success)
        }
    }

    function subscribe_to_newsletter_success(responseText, statusText, xhr, elem) {
        if (responseText['results'] == 'ok') {
            $("#modalNewsletterTitolo").html(title_modal_success_dialog);
            $(".modal-newsletter-form-body").html(responseText['message']);
            $(".modal-newsletter-form-header").css("background-color", "#5cb85c")
            modal.style.display = "block";
        }
        else {
            $("#modalNewsletterTitolo").html(title_modal_error_dialog);
            $(".modal-newsletter-form-body").html(responseText['message']);
            $(".modal-newsletter-form-header").css("background-color", "#b80a00")
            modal.style.display = "block";
        }
        $("#id_button_form_iscrizione_newsletter").attr("disabled", false);
        $("#id_button_form_iscrizione_newsletter").html(text_newsletter_button_enabled);
    }

    $(document).ready(function () {
        $("#id_button_form_iscrizione_newsletter").on('click', function (e) {
            e.preventDefault();
            subscribe_to_newsletter();
        });
    });
});