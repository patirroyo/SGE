public with sharing class RandomApex {
    public RandomApex() {

    }
    // Returns a random number between 0 (inclusive) and 1 (exclusive)
    @AuraEnabled //muy importante, sino no se puede llamar desde el front end de lightning component 
    public static Double random() {
        return Math.random();
    }

    @AuraEnabled
    public static Void insertScore(String nombre, String puntuacion){
        Account account = new Account(Name=nombre, BillingCity=puntuacion);//crea un nuevo registro de tipo Account
        insert account;//inserta el registro en la base de datos
    }

    @AuraEnabled
    public static List<Account> getListScores(){
        try{
            Account[] accounts = [SELECT Name, BillingCity FROM Account];
            return accounts;
        } catch(Exception e){
            throw new AuraHandledException('e.getMessage()');
        }
    }
}