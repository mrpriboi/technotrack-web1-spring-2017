$(document).ready(
    function() {
        $('.catselect').chosen();

        if ($(".commentsdiv").size() != 0) {
            window.setInterval(
                function() {
                    var el = $(".commentsdiv");
                    el.load(el.data('url'));
                },
                2000
            );

        };

        $(".likebutton").click(function() {
                var el = $(this);
                $.ajax({
                url: el.data('url'),
                success: function(data) {
                    $(".countlikes").html(data);
                }});

                // $(".likebutton").hide();
            }
        );

        if ($(".countlikes").size() != 0) {
            window.setInterval(
                function() {
                    $.ajax({
                        url: document.location.href + "countlikes",
                        success: function(data, textStatus, jqXHR) {
                            $(".countlikes")[0].innerHTML = data;
                        }
                    });
                },
                2000
            );
        }

        $(document).on('click', '.showModal', function () {
            $('.modal-body').load($(this).data('url'), function(){ $('select').chosen() });
            $('#myModal').modal('show');
            // setTimeout(function(){
            //     $('select').chosen();
            // }, 1000)

        });

        $(document).on("submit", ".ajax_add_post_form", function() {
            $.ajax({url: $(this).attr('action'), method: 'POST', data: $('form').serialize(),
            success: function(data, textStatus, jqXHR) {
                if (data == "OK") {
                    location.reload();
                } else {
                    $(".for_creating_post_form").html(data);
                }
            }});
            return false;
});

    }

)