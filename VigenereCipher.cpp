#include <bits/stdc++.h>
using namespace std;

string GenerateKey(string text, string key)
{
    int i = 0;
    while (key.size() != text.size())
    {
        key.push_back(key[i]);
        i++;
    }
    return key;
}

string VigenreCipherEncrypt(string text, string key)
{
    string ciphertext;
    for (int i = 0; i < text.size(); i++)
    {
        char x = (text[i] + key[i]) % 26;
        x += 'A';
        ciphertext.push_back(x);
    }
    return ciphertext;
}

string VigenreCipherDecrypt(string ciphertext, string key)
{
    string text;
    for (int i = 0; i < ciphertext.size(); i++)
    {
        char x = (ciphertext[i] - key[i] + 26) % 26;
        x += 'A';
        text.push_back(x);
    }
    return text;
}

int main()
{
    int option;
    string key, text, ciphertext;
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
    key = GenerateKey(text, key);
    ciphertext = VigenreCipherEncrypt(text, key);
    cout << "Cipher Text: " << ciphertext << endl;
    cout << "Original Text: " << VigenreCipherDecrypt(ciphertext, key);
    return 0;
}
