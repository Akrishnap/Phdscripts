#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

#define MAGIC_NUM 100

#define NEUELAB_VERSION                       _IOR(MAGIC_NUM,7,void *)
#define NEUELAB_TIMESTAMP                     _IOR(MAGIC_NUM,8,void *)
#define NEUELAB_GEN_REG                       _IOWR(MAGIC_NUM,6,void *)
#define NEUELAB_OUTNEUTHRESHOLD               _IOW(MAGIC_NUM,10,void *)


#define CTRL_REG 0x00
#define RXDATA_REG 0x08
#define RXTIME_REG 0x0C
#define TXDATA_REG 0x10
#define DMA_REG 0x14
#define RAWI_REG 0x18
#define IRQ_REG 0x1C
#define MASK_REG 0x20
#define BIAS_REG 0x24
#define STMP_REG 0x28
#define PRESC_REG 0x2C
#define OUTNEUTH_REG 0x30
#define ID_REG 0x5C


#define CTRL_ENABLEIP 0x00000001
#define CTRL_ENABLEINTERRUPT  0x00000004
#define CTRL_ENABLELOOPBACK 0x00000008
#define CTRL_FLUSHFIFO  0x00000010
#define CTRL_MN256CHIPTYPE  0x00010000



#define MSK_TIMEWRAPPING 0x00000080

typedef struct neuelab_gen_reg {
    unsigned int offset;
    char rw;
    unsigned int data;
}

neuelab_gen_reg_t;

void write_generic_neuelab_reg (int fp, unsigned int offset, unsigned int data) {
    neuelab_gen_reg_t reg;
    reg.rw=1;
    reg.data=data;
    reg.offset=offset;
    ioctl(fp,NEUELAB_GEN_REG,&reg);
}

unsigned int read_generic_neuelab_reg (int fp, unsigned int offset) {
    neuelab_gen_reg_t reg;
    reg.rw=0;
    reg.offset=offset;
    ioctl(fp,NEUELAB_GEN_REG,&reg);
    return reg.data;
}

void usage() {
    printf ("%s <even number of data to transfer> <output neuron threshold>\n", __FILE__);
    exit(1);
}



int main(int argc, char * argv[])
{
    int fp;
    FILE *f;
    unsigned long version;
    unsigned char hw_major,hw_minor;
    char stringa[4];
    int i;
    unsigned int *TXDATA, *RXDATA;
    int numdata=0;
    //int OutNumThreshold=0;
    int real_data;

//    if (argc==3) {
//        numdata=atoi(argv[1]);
//        if (numdata%2)
//            usage();
//        //OutNumThreshold=atoi(argv[2]);
//    }
//    else
//        usage();

    fp = open("/dev/neuelab", O_RDWR);
    if(fp < 0) {
        printf("Cannot open /dev/neuelab for write\n");
        return -1;
    }
    f=fopen("/home/icub/Desktop/addr_data_timestamp.txt","w");

    ioctl(fp,NEUELAB_VERSION,&version);
    hw_major=(version&0xF0)>>4;
    hw_minor=(version&0x0F) ;
    for (i=0;i<3;i++) {
        stringa[i]=(version&0xFF000000)>>24;
        version=version<<8;
    }
    printf ("\r\nIdentified: %s version %d.%d\r\n\r\n",stringa,hw_major,hw_minor);
    printf ("Times wrapping counter: %d\n",read_generic_neuelab_reg(fp,STMP_REG));

//    printf ("Output neuron threshold: %d\n",OutNumThreshold);
//    ioctl(fp,NEUELAB_OUTNEUTHRESHOLD,OutNumThreshold);
    // Enable Time wrapping interrupt
    write_generic_neuelab_reg(fp, MASK_REG, MSK_TIMEWRAPPING);

    // Flush FIFOs
    write_generic_neuelab_reg(fp, CTRL_REG,CTRL_FLUSHFIFO);

    write_generic_neuelab_reg(fp, CTRL_REG,CTRL_ENABLEIP);



        // Allocate memory for receiving buffer
    RXDATA=(unsigned int *) calloc(1024,sizeof(unsigned int));

    //write (fp, (char *)TXDATA, numdata*sizeof(unsigned int));
    while (1){
    printf("Now read...\n");
    real_data=read (fp, (char *)RXDATA, numdata*sizeof(unsigned int));

    // Show data
    for (i=0; i<real_data/sizeof(unsigned int); i+=2)
       // fprintf(f,"%4d 0x%08x 0x%08x\n",i , RXDATA[i+1], RXDATA[i]);
        printf("%4d 0x%08x 0x%08x\n",i , RXDATA[i+1], RXDATA[i]);
    }

    // Stop IP

//    write_generic_neuelab_reg(fp, CTRL_REG, CTRL_ENABLEINTERRUPT );
//    printf ("Times wrapping counter: %d\n",read_generic_neuelab_reg(fp,STMP_REG));

    close(fp);
    //free (TXDATA);
    free (RXDATA);
    return 0;
}
