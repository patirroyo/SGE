({
    doInit : function(component, event, helper) {
        
    },

    rock : function(component, event, helper) {
        //alert('You selected Rock');
        component.set("v.playerChoice", "Rock");
    },
    paper : function(component, event, helper) {
        //alert('You selected Paper');
        component.set("v.playerChoice", "Paper");
    },
    scissors : function(component, event, helper) {
        //alert('You selected Scissors');
        component.set("v.playerChoice", "Scissors");
    },
    player1 : function(component, event, helper) {
        //alert('You selected Player 1');
        component.set("v.playerNumber", 1);
    },
    player2 : function(component, event, helper) {
        alert('You selected Player 2');
        component.set("v.playerNumber", 2);
    },
    play : function(component, event, helper) {
        var playerChoice = component.get("v.playerChoice");
        var playerNumber = component.get("v.playerNumber");
        var round = component.get("v.round");
        var insertRoundApex = component.get("c.insertRound");
        alert("playerChoice: " + playerChoice + " playerNumber: " + playerNumber + " round: " + round);
        insertRoundApex.setCallback(this, function(response){
            var state = response.getState();
            if(state === "SUCCESS"){
                alert("exito")
            }
        });

        insertRoundApex.setParams({
            "round": round,
            "playerNumber": playerNumber,
            "playerChoice": playerChoice,
        });
        $A.enqueueAction(insertRoundApex);
    }


})
