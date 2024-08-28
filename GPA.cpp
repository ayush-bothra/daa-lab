#include<iostream>
#include<vector>
using namespace std;

vector<float> calc_SPI(vector<vector<vector<int>>> sem,int n)
{
    vector<float> SPI_store;
    if(n > sem.size()) return {-1}; // more sems queried than given.
    if(sem.size() == 0) return {}; // if no sems are provided

    for(int i = 0; i < n; i++)
    {
        float sum = 0; float count = 0;
        for(int j = 0; j < sem[i].size(); j++)
        {
            if(sem[i][j][1] > 10 || sem[i][j][0] > 4) return {-1}; // if grade scores are greater than 10 points or credits greater than 4
            if(sem[i][j][1] < 0 || sem[i][j][0] < 0) return {-1}; // if grade or credit scores are negative
            sum += sem[i][j][0] * sem[i][j][1];
            count += sem[i][j][0];
        }
        SPI_store.push_back((sum/count));
    }
    return SPI_store;
}

float calc_CPI(vector<vector<vector<int>>> sem,int n)
{
    vector<float> values = calc_SPI(sem,n);
    if(values.size() == 0) return 0;
    if(values[0] == -1) return -1;
    float sum = 0; float count = 0;

    for(const auto& value : values) // goes thru each value present in the array
    {
        sum += value;
        count = count + 1.0;
    }
    float CPI_value = sum/count;
    return CPI_value;
}

int main()
{
    vector<vector<vector<int>>> store = {{{2,9},{4,7},{2,8}},{{3,7},{1,10},{2,5}}}; // hard code the values to run the program
    int n = 2;
    float cpi = calc_CPI(store, n);
    cout << cpi << "\n";
    return 0;
}