#include <bits/stdc++.h>
using namespace std;

string CaesarCipherEncrypt(string text, int key)
{
    string ciphertext = "";
    for (int i = 0; i < text.length(); i++)
    {
        ciphertext += char(int(text[i] + key - 65) % 26 + 65);
    }
    return ciphertext;
};

int main()
{
    int option, key;
    string text;
    cout << "Enter option:\n1)Console\n2)File\n";
    cin >> option;
    cout << "Enter key: ";
    cin >> key;
    switch (option)
    {
    case 1:
        cout << "Enter text: ";
        break;
    case 2:
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        break;
    }
    cin >> text;
    cout << "Cipher Text: " << CaesarCipherEncrypt(text, key);
    return 0;
}
