$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1, // Numerical value
        speed: 0.30, // Numerical value
        autostart: true
    });

    // mic button click event
    $("#MicBtn").click(function () { // Correct syntax
        eel.play_startup_sound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.all_commands(); // Removed extra parentheses
    });

    function doc_keyUp(e) {
        // this would test for whichever key is 'j' (down arrow) and the ctrl key at the same time
        if (e.key === 'j' && e.metaKey) {
            eel.play_startup_sound();
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.all_commands(); // Removed extra parentheses
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message) {
        if (message != "") {
            $("#Oval").attr("hidden", true); // Fixed selector - added #
            $("#SiriWave").attr("hidden", false);
            eel.all_commands(message); // Pass message correctly
            $("#chatbox").val("");
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }

    function ShowHideButton(message) {
        if (message.length === 0) { // Added curly braces for consistency
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        } else {
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }

// key up event handler on text box
$("#chatBox").keyup(function () {

    let message = $("#chatBox").val();
    ShowHideButton(message)

});

// send button event handler
$("#SendBtn").click(function () {

    let message = $("#chatBox").val()
    PlayAssistant(message)

});


// enter press event handler on chat box
$("#chatBox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
        let message = $("#chatBox").val()
        PlayAssistant(message)
    }
});


});
