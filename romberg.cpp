#include <bits/stdc++.h>
using namespace std;
#define PI M_PI

double f_1(double x, double h){
    return cos(x*h);
}

double f_2(double x, double h){
    return pow(x*h, 2);
}

double trapezoidal_1(int m){
    double h = (PI/2) / m;
    double sum = 0;
    for(int i = 0; i <= m; i++){
        if(i == 0 || i == m){
            sum += f_1(i, h);
        }else{
            sum += f_1(i, h) * 2;
        }
    }
    return sum * h / 2;
}

double trapezoidal_2(int m){
    double h = 1.0 / m;
    double sum = 0;
    for(int i = 0; i <= m; i++){
        if(i == 0 || i == m){
            sum += f_2(i, h);
        }else{
            sum += f_2(i, h) * 2;
        }
    }
    return sum * h / 2;
}

double romberg_1(int i, int j){
    if(j == 0){
        return trapezoidal_1(pow(2, i));
    }else{
        return (pow(4, j) * romberg_1(i, j-1) - romberg_1(i-1, j-1)) / (pow(4, j) - 1);
    }
}

double romberg_2(int i, int j){
    if(j == 0){
        return trapezoidal_2(pow(2, i));
    }else{
        return (pow(4, j) * romberg_2(i, j-1) - romberg_2(i-1, j-1)) / (pow(4, j) - 1);
    }
}

int main(){
    cout << "Trapezoidal untuk fungsi 1" << endl;
    for(int i=1; i<=10; i++){
        cout << i << " " << trapezoidal_1(i) << endl;
    }

    cout << endl;

    cout << "Trapezoidal untuk fungsi 2" << endl;
    for(int i=1; i<=10; i++){
        cout << i << " " << trapezoidal_2(i) << endl;
    }

    cout << "\n" << "romberg list untuk fungsi 1" << endl;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            if(j <= i){
                cout << romberg_1(i, j) << " ";
            }else{
                cout << " ";
            }
        }
        cout << endl;
    }

    cout << "\n" << "romberg list untuk fungsi 2" << endl;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            if(j <= i){
                cout << romberg_2(i, j) << " ";
            }else{
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}