public with sharing class GameStoreService {
    @AuraEnabled(cacheable=true)
    public static List<GameStore__c> getRecords() { 
        try {
            // Create a list of GameStore records from a SOQL query
            List<GameStore__c> lstGameStores = [
                SELECT
                    Id,
                    Name,
                    Address__c,
                    State__c, 
                    City__c,
                    Zip__c
                    FROM GameStore__c
                    WITH SECURITY_ENFORCED
                    ORDER BY CreatedDate
                    LIMIT 10
                ];
            return lstGameStores;
        }
        // Code to handle exception
        catch (Exception e) {
            throw new AuraHandledException(e.getMessage());
        }
    }
}