public with sharing class RandomApex {
    public RandomApex() {

    }

    // Returns a random number between 0 (inclusive) and 1 (exclusive)
    @AuraEnabled //muy importante, sino no se puede llamar desde el front end de lightning component 
    public static Double random() {
        return Math.random();
    }
}