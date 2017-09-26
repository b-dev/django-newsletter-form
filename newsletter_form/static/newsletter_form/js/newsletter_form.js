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
        var div_errore_email_newsletter = $("#id_error_form_iscrizione_newsletter");

        if (email_address == '') {
            div_errore_email_newsletter.show();
        } else {
            div_errore_email_newsletter.hide();
            button_newsletter.attr("disabled", true);
            button_newsletter.html(text_newsletter_button_disabled);
            $.post(url_iscrizione_newsletter, {'csrfmiddlewaretoken': csrftoken,
                                               'email_newsletter': email_address}, subscribe_to_newsletter_success)
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