#include <iostream>
#include <fstream>


using namespace std;


int main() {

    char stac[10];
    long k = 0;

    int ch = 0;
    char x;
    string line = "";
    ifstream fin("brackets.in");
    ofstream fout("brackets.out");


    do{
        x = fin.get();
        if ( ch == 1 and x != '\n')
        {
            continue;
        }
        if ( x == '(' or x == '[')
        {
            stac[k] = x;
            k += 1;
        }
        else
            {
                if ( x == ')')
                {
                    if ( stac[k-1] == '(')
                    {
                        k -= 1;
                    }
                    else
                        {
                            ch = 1;
                        }
                }
                else
                    {
                        if ( x == ']')
                        {
                            if ( stac[k-1] == '[')
                            {
                                k -= 1;
                            }
                            else
                                {
                                    ch = 1;
                                }
                        }
                    }
            }

        if ( ch == 0 and  k == 0 and (x == '\n' or x == EOF))
        {
            ch = 0;
            fout << "YES\n";
        }
        if ( (k != 0 or ch == 1) and (x == '\n' or x == EOF))
        {
            ch = 0;
            fout << "NO\n";
        }
    } while ( x != EOF);

    fout << line;

    fout.close();
    fin.close();
    return 0;
}
