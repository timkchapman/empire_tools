$(document).ready(function () {
    $('#conversionForm').on('submit', function (event) {
        event.preventDefault();

        var rings = parseInt($('#rings').val()) || 0;
        var crowns = parseInt($('#crowns').val()) || 0;
        var thrones = parseInt($('#thrones').val()) || 0;
        var output_unit = $('#output_unit').val();

        $.ajax({
            url: '/calculate',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                rings: rings,
                crowns: crowns,
                thrones: thrones,
                output_unit: output_unit
            }),
            success: function (response) {
                var result = response.result;
                var formattedResult = '';

                if (result.thrones && result.thrones !== 0) {
                    formattedResult += result.thrones + ' Thrones';
                    if ((result.crowns && result.crowns !== 0) || (result.rings && result.rings !== 0)) {
                        formattedResult += ', ';
                    }
                }
                if (result.crowns && result.crowns !== 0) {
                    formattedResult += result.crowns + ' crowns';
                    if (result.rings && result.rings !== 0) {
                        formattedResult += ', ';
                    }
                }
                if (result.rings && result.rings !== 0) {
                    formattedResult += result.rings + ' rings';
                }

                $('#result').html('<h4>Converted Result: ' + formattedResult + '</h4>');
            }
        });
    });
});
