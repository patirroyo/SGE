({
    myAction: function (component, event, helper) {

    },
    handleEvent: function (component, event, helper) {
        var pointsToAdd = event.getParam("molePoint");
        //console.log('pointsToAdd: ' + pointsToAdd);
        var marcador = component.get("v.marcador");
        //console.log('marcador: ' + marcador);
        if (pointsToAdd == 0) {
            marcador = 0;
        } else {
            marcador = marcador + pointsToAdd;
        }
        component.set("v.marcador", marcador);
    },
    guardarScore: function (component, event, helper) {//vamos a usar el apex
        var insertScoreApex = component.get("c.insertScore");//llamamos al metodo de apex insertScore que es propia de salesforce
        var nombre = component.find("nombre").getElement().value;//busco con el aura:id nombre
        console.log("nombre: " + nombre);
        insertScoreApex.setCallback(this, function (response) {//llamamos setCallback para que nos devuelva el resultado
            var state = response.getState();
            if (state === "SUCCESS") {
                alert("exito")
            }
        });

        insertScoreApex.setParams({
            "nombre": nombre,
            "puntuacion": component.get("v.marcador")
        });


        $A.enqueueAction(insertScoreApex);

    },
})
