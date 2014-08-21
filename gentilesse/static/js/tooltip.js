function showTooltip(x, y, contents) {
    $('<div id="tooltip">' + contents + '</div>').css({
        position: 'absolute',
        display: 'none',
        top: y + 5,
        left: x + 20,
        border: '2px solid #4572A7',
        padding: '2px',    
        size: '10',  
        'background-color': '#fff',
        opacity: 0.80
    }).appendTo("body").fadeIn(200);
}
