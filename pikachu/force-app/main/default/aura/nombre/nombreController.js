({
    myAction : function(component, event, helper) {

    }, 
    saludar : function(component, event, helper) {
        alert("antes eras " + component.get("v.nombreOld") + " y ahora eres "+ component.get("v.nombre"));
        //trigers an event
        var evt = $A.get("e.c:evtData"); //cojo el evento que existe
        var obj = {//creo un objeto con los datos que quiero pasar
            "nombre" : component.get("v.nombre"),
            "apellido" : "Alert!!!"
        };

        evt.setParams(obj); // cargo los datos en el evento
        component.set("v.nombreOld", component.get("v.nombre"))
        evt.fire(); //enviar el evento para que lo escuche alguien
    }
})
