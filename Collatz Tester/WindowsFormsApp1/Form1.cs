using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        private string a;
        private string input;
        private int temp;

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text = textBox1.Text;
            int input = int.Parse(textBox1.Text);
            int temp = input;
            while (temp > 1)
            { 
                if (temp % 2 == 0)
                {
                    temp = temp / 2;
                }
                else
                {
                    temp = temp * 3 + 1;
                }
                textBox2.Text = textBox2.Text + "," + temp;
            }
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
