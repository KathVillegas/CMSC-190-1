//javac AttendanceFaceDetection.java
//java AttendanceFaceDetection

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.io.*;

public class AttendanceFaceRecognition{
	
	static final JFrame frame = new JFrame("Attendance Face Recognition");

	static JPanel panel = new JPanel();
	static JPanel buttonPanel = new JPanel();

	static JButton uploadButton = new JButton("Upload Image");
	static JButton processButton = new JButton("Process");

	static JLabel subjectLabel = new JLabel("SUBJECT: ");
	static JLabel sectionLabel = new JLabel("SECTION: ");
	static JLabel note = new JLabel("NOTE: Inputs should not have spaces.", SwingConstants.CENTER);

	static JTextField subjectField = new JTextField(20);
	static JTextField sectionField = new JTextField(10); 

	static String fileName;
	static String subject;
	static String section;

	public static void main(String[] args){
		
		frame.setResizable(false);
		frame.setLayout(new BorderLayout());

		panel.setPreferredSize(new Dimension(400,100));
		buttonPanel.setPreferredSize(new Dimension(400,50));

		GroupLayout layout = new GroupLayout(panel);
		panel.setLayout(layout);
		buttonPanel.setLayout(new GridBagLayout());

		GridBagConstraints a = new GridBagConstraints();
		a.fill = GridBagConstraints.HORIZONTAL;
		a.insets = new Insets(2,2,2,5);

		uploadButton.setPreferredSize(new Dimension(150,30));
		processButton.setPreferredSize(new Dimension(150,30));
		buttonPanel.add(uploadButton, a);
		buttonPanel.add(processButton, a);

		layout.setAutoCreateGaps(true);
		layout.setAutoCreateContainerGaps(true);

		layout.setHorizontalGroup(
		   layout.createSequentialGroup()
		   		.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
			      .addComponent(subjectLabel)
			      .addComponent(sectionLabel)
			      )	
			    .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
			      .addComponent(subjectField)
			      .addComponent(sectionField)   	
			      )	
		);

		layout.setVerticalGroup(
		   layout.createSequentialGroup()
		      .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
		           .addComponent(subjectLabel)
		           .addComponent(subjectField)
		       )
		      .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
		           .addComponent(sectionLabel)
		           .addComponent(sectionField)
		       )
		);

		//upload button
		uploadButton.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent a1){
				JFileChooser chooser = new JFileChooser();
				int returnVal = chooser.showOpenDialog(frame);

				if (returnVal == JFileChooser.APPROVE_OPTION) {
					fileName = chooser.getSelectedFile().getAbsolutePath();
				}

			}
		});
		//process button
		processButton.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent a2){
				try{
					int flag = 0;
					String command;

					
					if(subjectField.getText().equals("")){
						JOptionPane.showMessageDialog(frame,"Please specify the subject!","Warning", JOptionPane.WARNING_MESSAGE);
						flag = 1;
					}
					if(sectionField.getText().equals("")){
						JOptionPane.showMessageDialog(frame,"Please specify the section!","Warning", JOptionPane.WARNING_MESSAGE);
						flag = 1;
					}
					if(fileName == null){
						JOptionPane.showMessageDialog(frame,"Please include an image!","Warning", JOptionPane.WARNING_MESSAGE);
						flag = 1;
					}
					if(flag == 0){
						subject = subjectField.getText();
						section = sectionField.getText();

						//this will execute the python face detection
						command = "python AttendanceFaceRecognition.py " + fileName +" "+ subject +" "+ section;
						System.out.println(command);
						Runtime.getRuntime().exec(command);	
					}
				}
				catch(Exception err){
					err.printStackTrace();
				}
			}
		});

		note.setForeground(Color.red);
		frame.add(panel, BorderLayout.NORTH);
		frame.add(note, BorderLayout.CENTER);
		frame.add(buttonPanel, BorderLayout.SOUTH);
		frame.setVisible(true);
		frame.pack();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
