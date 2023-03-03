#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BRACKET_SIZE 7

double idahoBrackets[BRACKET_SIZE][3] = { // single
    {0, 1540, .0112},
    {1541, 3080, .0312},
    {3081, 4621, .0362},
    {4622, 6161, .0462},
    {6162, 7702, .0562},
    {7703, 11553, .0662},
    {11554, 1000000000, .0692}
};

double fedBrackets[BRACKET_SIZE][3] = { // single
    {0, 10275, .1},
    {10276, 41775, .12},
    {41776, 89075, .22},
    {89076, 170050, .24},
    {170051, 215950, .32},
    {215951, 539900, .35},
    {359901, 1000000000, .37}
};

const char spacer[] = "========================================";

double ProvideSalary() {
    char salary[20];
    printf("How much do you make annually?:\t");
    fgets(salary, sizeof(salary), stdin);
    int len = strlen(salary);
    double filteredSalary = 0;
    for (int i = 0; i < len; i++) {
        if (salary[i] >= '0' && salary[i] <= '9') {
            filteredSalary = filteredSalary * 10 + (salary[i] - '0');
        }
    }
    return filteredSalary;
}

double CalculateTaxes(double income, double brackets[][3]) {
    double taxes = 0;
    for (int i = 0; i < BRACKET_SIZE; i++) {
        double bottom = brackets[i][0];
        double top = brackets[i][1];
        double amount = brackets[i][2];
        if (income > top) {
            taxes += (top - bottom) * amount;
        } else {
            taxes += (income - bottom) * amount;
            break;
        }
    }
    return round(taxes * 100) / 100;
}

void Budget(double grossIncome) {
    double idahoTaxes = CalculateTaxes(grossIncome, idahoBrackets);
    double fedTaxes = CalculateTaxes(grossIncome, fedBrackets);
    double netIncome = grossIncome - idahoTaxes - fedTaxes;
    printf("\n%s\nTAX EST.", spacer);
    printf("\nGross Income: ------------- $%.02f", grossIncome);
    printf("\nIdaho Taxes: -------------- [$%.02f", idahoTaxes);
    printf("]\nFederal Taxes: ------------ [$%.02f", fedTaxes);
    printf("]\nNet Income: --------------- $%.02f\n", netIncome);
    printf(spacer);
    printf("\n");
}

int main() {
    Budget(ProvideSalary());
}
