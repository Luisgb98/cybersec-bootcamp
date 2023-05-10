/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   shellcode.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lguisado <lguisado@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/09 23:00:32 by lguisado          #+#    #+#             */
/*   Updated: 2023/05/09 23:00:32 by lguisado         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <windows.h>

int main () {
    __asm{
        ; LoadLibrary("msvcrt.dll")
		
        push ebp      ; dirección base de la pila
        mov  ebp, esp ; mueve la pila para crear una nueva que apunte a esp
        xor  edi, edi ; efectuar bit por bit la disyunción exclusiva lógica
        push edi
		
        sub  esp, 0Ch ; asigna 12 bytes de memoria
		
        mov byte ptr [ebp-0Bh], 6Dh     ; m
        mov byte ptr [ebp-0Ah], 73h     ; s
        mov byte ptr [ebp-09h], 76h     ; v
        mov byte ptr [ebp-08h], 63h     ; c
        mov byte ptr [ebp-07h], 72h     ; r
        mov byte ptr [ebp-06h], 74h     ; t
        mov byte ptr [ebp-05h], 2Eh     ; .
        mov byte ptr [ebp-04h], 64h     ; d
        mov byte ptr [ebp-03h], 6Ch     ; l
        mov byte ptr [ebp-02h], 6Ch     ; l
		
        lea eax, [ebp-0Bh]              ; Ultima posicion de 'msvcrt.dll'
		
        push eax
        mov ebx,0x7c801d7b              ; Direccion de memoria de la libreria 'LoadLibrary'
        call ebx                        ; Sacada con offset.c
		
		
        ; system(calc.exe)
		
        push ebp
        mov  ebp, esp
        xor  edi, edi
        push edi
		
        sub  esp, 08h   ; asigna 12 bytes de memoria
		
        mov byte ptr [ebp-09h], 63h     ; c
        mov byte ptr [ebp-08h], 61h     ; a
        mov byte ptr [ebp-07h], 6Ch     ; l
        mov byte ptr [ebp-06h], 63h     ; c
        mov byte ptr [ebp-05h], 2Eh     ; .
        mov byte ptr [ebp-04h], 65h     ; e
        mov byte ptr [ebp-03h], 78h     ; x
        mov byte ptr [ebp-02h], 65h     ; e
		
        lea eax, [ebp-09h]              ; Ultima posicion de 'calc.exe'
		
        push eax
        mov  ebx, 0x77c293c7            ; Direccion de memoria de la libreria 'system'
        call ebx                        ; Sacada con offset.c
    }
}