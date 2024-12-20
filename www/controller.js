$(document).ready(function () {
    // Expose the DisplayMessage function to Python
    
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

    eel.expose(updateChatCanvasSender);
    function updateChatCanvasSender(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
        chatBox.innerHTML += `
            <div class="row justify-content-end mb-4">
                <div class="width-size">
                    <div class="sender_message">${message}</div>
                </div>
            </div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

    eel.expose(updateChatCanvasReceiver);
    function updateChatCanvasReceiver(message) {
    var chatBox = document.getElementById("chat-canvas-body");
    if (message.trim() !== "") {
        chatBox.innerHTML += `
            <div class="row justify-content-start mb-4">
                <div class="width-size">
                    <div class="receiver_message">${message}</div>
                </div>
            </div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

});
