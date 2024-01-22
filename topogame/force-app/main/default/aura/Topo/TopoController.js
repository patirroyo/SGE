
({
    doInit: function(cmp) {
        var topo = cmp.find("topo");
        //Math.random() < 0.5 ? $A.util.addClass(topo, 'active') : $A.util.addClass(topo, 'inactive') ;
        
        var number =Math.random() ;
        if(number < 0.5){
            $A.util.addClass(topo, 'active');
            cmp.set("v.isTopo", true)//para recuperar la variable de la vista isTopo y poder usarla en el componente
        }else{
            $A.util.addClass(topo, 'inactive');
            cmp.set("v.isTopo", false) //para recuperar la variable de la vista isTopo y poder usarla en el componente, la usaré para decir si el usuario ha acertado o no
        }
    
    },
    topoClick: function(cmp, event, helper){//esta función va a disparar un evento
        // this function trigger an event
        var isTopo = cmp.get("v.isTopo");//recupero la variable de la vista isTopo
        //console.log('isTopo: ' + isTopo);
        var evt = $A.get("e.c:Puntuacion");//recupero el evento que he creado en el componente Puntuacion
        //console.log('evt: ' + evt);
        evt.setParams({//setParams es para pasarle parámetros al evento
            "molePoint": isTopo ? 2 : 0 //si isTopo es true, es que el usuario ha acertado, por lo que le sumo un punto, si no, le resto un punto
        });
        //console.log('molesPoint: ' + evt.getParam("molePoint"));
        evt.fire();//fire es para lanzar el evento
    }
})

