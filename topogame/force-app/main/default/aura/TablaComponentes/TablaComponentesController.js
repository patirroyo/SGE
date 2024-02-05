({
    myAction: function (component, event, helper) {
    },
    doInit: function (component) {

        var getListScores = component.get("c.getListScores")

        getListScores.setCallback(this, function (response) {
            var estadoDeLaPeticion = response.getState();
            if (estadoDeLaPeticion === "SUCCESS") {
                var accounts = response.getReturnValue();
                component.set("v.puntuaciones", accounts)

            }
        });
        $A.enqueueAction(getListScores);
    }
})
