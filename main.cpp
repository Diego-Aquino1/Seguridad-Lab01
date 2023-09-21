#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

// Función para realizar las sustituciones en el texto
void sustituirCaracteres(string& texto) {
    for (size_t i = 0; i < texto.size(); i++) {
        if (texto[i] == 'j' || texto[i] == 'h') {
            texto[i] = 'i';
        } else if (texto[i] == 'ñ') {
            texto[i] = 'n';
        } else if (texto[i] == 'k') {
            texto[i] = 'l';
        } else if (texto[i] == 'u' || texto[i] == 'w') {
            texto[i] = 'v';
        } else if (texto[i] == 'y') {
            texto[i] = 'z';
        }
    }
}
// Función para eliminar tildes
void eliminarTildes(string& texto) {
    for (size_t i = 0; i < texto.size(); i++) {
        switch (texto[i]) {
            case 225: texto[i] = 'a'; break; // á
            case -87: texto[i] = 'e'; break; // é
            case 237: texto[i] = 'i'; break; // í
            case 243: texto[i] = 'o'; break; // ó
            case 250: texto[i] = 'u'; break; // ú
            case 193: texto[i] = 'A'; break; // Á
            case 201: texto[i] = 'E'; break; // É
            case 205: texto[i] = 'I'; break; // Í
            case 211: texto[i] = 'O'; break; // Ó
            case 218: texto[i] = 'U'; break; // Ú
        }
    }
}

// Función para convertir a mayúsculas
void convertirAMayusculas(string& texto) {
    transform(texto.begin(), texto.end(), texto.begin(), ::toupper);
}

// Función para eliminar espacios en blanco y signos de puntuación
void eliminarEspaciosPuntuacion(string& texto) {
    texto.erase(remove_if(texto.begin(), texto.end(), ::isspace), texto.end());
    texto.erase(remove_if(texto.begin(), texto.end(), ::ispunct), texto.end());
}

int main() {
    ifstream archivoEntrada("D:/UNSA/4/Seguridad/Seguridad-Lab01/text.txt");
    if (!archivoEntrada.is_open()) {
        cerr << "No se pudo abrir el archivo de entrada." << endl;
        return 1;
    }

    string texto;
    string linea;
    while (getline(archivoEntrada, linea)) {
        texto += linea + '\n';
    }

    // Realizar las operaciones de preprocesamiento
    sustituirCaracteres(texto);
    eliminarTildes(texto);
    convertirAMayusculas(texto);
    eliminarEspaciosPuntuacion(texto);

    // Guardar el resultado en el archivo de salida
    ofstream archivoSalida("D:/UNSA/4/Seguridad/Seguridad-Lab01/HERALDOSNEGROSpre.txt");
    if (!archivoSalida.is_open()) {
        cerr << "No se pudo abrir el archivo de salida." << endl;
        return 1;
    }

    archivoSalida << texto;

    archivoEntrada.close();
    archivoSalida.close();

    cout << "Operaciones de preprocesamiento completadas. Resultado guardado en 'HERALDOSNEGROS pre.txt'." << endl;

    return 0;
}