/* Generated by Nim Compiler v0.17.2 */
/*   (c) 2017 Andreas Rumpf */
/* The generated code is subject to the original license. */
/* Compiled for: Windows, amd64, gcc */
/* Command for C compiler:
   C:\nim-0.17.2\dist\mingw64\bin\gcc.exe -c  -w -mno-ms-bitfields  -IC:\nim-0.17.2\lib -o c:\webdev\dmlauto\nim\hello\nimcache\stdlib_sharedlist.o c:\webdev\dmlauto\nim\hello\nimcache\stdlib_sharedlist.c */
#define NIM_NEW_MANGLING_RULES
#define NIM_INTBITS 64

#include "nimbase.h"
#include <windows.h>
#include <string.h>
#undef LANGUAGE_C
#undef MIPSEB
#undef MIPSEL
#undef PPC
#undef R3000
#undef R4000
#undef i386
#undef linux
#undef mips
#undef near
#undef powerpc
#undef unix
typedef struct tyObject_SharedList_9cWkTIPQvNw7gFHMOEzMCLw tyObject_SharedList_9cWkTIPQvNw7gFHMOEzMCLw;
typedef struct tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw;
struct tyObject_SharedList_9cWkTIPQvNw7gFHMOEzMCLw {
tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw* head;
tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw* tail;
CRITICAL_SECTION lock;
};
typedef void* tyArray_Rrw59cMvNu8cDA9cQDh4v2oA[100];
struct tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw {
tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw* next;
NI dataLen;
tyArray_Rrw59cMvNu8cDA9cQDh4v2oA d;
};
static N_INLINE(void, initLock_NXoRcxfV39aV9cflSTUwtJ1glocks)(CRITICAL_SECTION* lock);
N_NIMCALL(void, acquire_9bBEZeGCRkWQl9bLT1qt423Q)(CRITICAL_SECTION* lock);
N_NOCONV(void*, allocShared0_sVm4rDImKK2ZDdylByayiA_3)(NI size);
N_NIMCALL(void, release_9bBEZeGCRkWQl9bLT1qt423Q_2)(CRITICAL_SECTION* lock);
static N_INLINE(void, nimFrame)(TFrame* s);
N_NOINLINE(void, stackOverflow_II46IjNZztN9bmbxUD8dt8g)(void);
static N_INLINE(void, popFrame)(void);
extern NIM_THREADVAR TFrame* framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw;

static N_INLINE(void, initLock_NXoRcxfV39aV9cflSTUwtJ1glocks)(CRITICAL_SECTION* lock) {
	InitializeCriticalSection(lock);
}

N_NIMCALL(tyObject_SharedList_9cWkTIPQvNw7gFHMOEzMCLw, initSharedList_ftyWlQN9a0f9cDyTF3NRz9cTg)(void) {
	tyObject_SharedList_9cWkTIPQvNw7gFHMOEzMCLw result;
	memset((void*)(&result), 0, sizeof(result));
	initLock_NXoRcxfV39aV9cflSTUwtJ1glocks((&result.lock));
	result.head = NIM_NIL;
	result.tail = NIM_NIL;
	return result;
}

N_NIMCALL(void, add_LMD14ZZveJ1hTQDkuvr6bQ)(tyObject_SharedList_9cWkTIPQvNw7gFHMOEzMCLw* x, void* y) {
	tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw* node;
	acquire_9bBEZeGCRkWQl9bLT1qt423Q((&(*x).lock));
	node = (tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw*)0;
	{
		NIM_BOOL T3_;
		void* T7_;
		T3_ = (NIM_BOOL)0;
		T3_ = ((*x).tail == NIM_NIL);
		if (T3_) goto LA4_;
		T3_ = ((*(*x).tail).dataLen == ((NI) 100));
		LA4_: ;
		if (!T3_) goto LA5_;
		T7_ = (void*)0;
		T7_ = allocShared0_sVm4rDImKK2ZDdylByayiA_3(((NI) (((NI)sizeof(tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw)))));
		node = ((tyObject_SharedListNodecolonObjectType__82xHhBDm9bpijSPOyEGz0Hw*) (T7_));
		(*node).next = (*x).tail;
		(*x).tail = node;
		{
			if (!((*x).head == NIM_NIL)) goto LA10_;
			(*x).head = node;
		}
		LA10_: ;
	}
	goto LA1_;
	LA5_: ;
	{
		node = (*x).tail;
	}
	LA1_: ;
	(*node).d[((*node).dataLen)- 0] = y;
	(*node).dataLen += ((NI) 1);
	release_9bBEZeGCRkWQl9bLT1qt423Q_2((&(*x).lock));
}

static N_INLINE(void, nimFrame)(TFrame* s) {
	NI T1_;
	T1_ = (NI)0;
	{
		if (!(framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw == NIM_NIL)) goto LA4_;
		T1_ = ((NI) 0);
	}
	goto LA2_;
	LA4_: ;
	{
		T1_ = ((NI) ((NI16)((*framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw).calldepth + ((NI16) 1))));
	}
	LA2_: ;
	(*s).calldepth = ((NI16) (T1_));
	(*s).prev = framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw;
	framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw = s;
	{
		if (!((*s).calldepth == ((NI16) 2000))) goto LA9_;
		stackOverflow_II46IjNZztN9bmbxUD8dt8g();
	}
	LA9_: ;
}

static N_INLINE(void, popFrame)(void) {
	framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw = (*framePtr_HRfVMH3jYeBJz6Q6X9b6Ptw).prev;
}
NIM_EXTERNC N_NOINLINE(void, stdlib_sharedlistInit000)(void) {
	nimfr_("sharedlist", "sharedlist.nim");
	popFrame();
}

NIM_EXTERNC N_NOINLINE(void, stdlib_sharedlistDatInit000)(void) {
}

