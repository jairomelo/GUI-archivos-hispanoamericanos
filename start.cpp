#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

int main() {
    char cwd[1024];
#ifdef _WIN32
    if (GetCurrentDirectory(sizeof(cwd), cwd) != 0) {
        strcat(cwd, "\\scripts");  // Agrega el subdirectorio 'scripts'
        if (SetCurrentDirectory(cwd) == 0) {
            printf("Error: No se pudo establecer el directorio de trabajo actual.\n");
            return 1;
        }
    } else {
        printf("Error: No se pudo obtener el directorio de trabajo actual.\n");
        return 1;
    }
#else
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        strcat(cwd, "/scripts");  // Agrega el subdirectorio 'scripts'
        if (chdir(cwd) != 0) {
            printf("Error: No se pudo establecer el directorio de trabajo actual.\n");
            return 1;
        }
    } else {
        printf("Error: No se pudo obtener el directorio de trabajo actual.\n");
        return 1;
    }
#endif

    system("lanzar.bat");
    return 0;
}
