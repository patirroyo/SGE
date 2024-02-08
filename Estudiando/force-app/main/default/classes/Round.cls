public with sharing class Round {
    public Round() {

    }
    @AuraEnabled
    public static Void insertRound(Integer round, String playerNumber, String playerChoice){
        Account acc = new Account(NumberOfEmployees = round, Name = playerNumber, BillingCity = playerChoice);
        insert acc;
    }

    @AuraEnabled
    public static List<Account> getListScores(){
        try {
            Account[] accounts = [SELECT NumberOfEmployees, Name, BillingCity FROM Account];
            return accounts;
        } catch (Exception e) {
            throw new AuraHandledException(e.getMessage());
        }
    }

}