({
    myAction : function(component, event, helper) {

    },
    handleEvent : function(component, event, helper) {
        var pointsToAdd = event.getParam("molePoint");
        //console.log('pointsToAdd: ' + pointsToAdd);
        var marcador = component.get("v.marcador");
        //console.log('marcador: ' + marcador);
        if (pointsToAdd == 0) {
            marcador = 0;
        }else{
            marcador = marcador + pointsToAdd;
        }
        component.set("v.marcador", marcador);
    }
})
