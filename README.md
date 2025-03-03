# CCWC - Command Line Word Count Tool  

## **Overview**
CCWC is a command-line utility inspired by the Unix `wc` command, designed for counting words, lines, characters, and more in text files. This was developed as a **challenge project**, and currently, it only supports `.txt` files. Future enhancements will include support for other file types.

## **Installation & Setup**
### **1. Add `WCTool` to the System Path**
Before using CCWC, you must add `WCTool` to your system's **Path Environment Variable**:
- **Windows:**  
  1. Open **System Properties** (`Win + R`, then type `sysdm.cpl` and press Enter).
  2. Go to the **Advanced** tab and click **Environment Variables**.
  3. Under **System variables**, find **Path**, select it, and click **Edit**.
  4. Click **New**, then enter the full path to your `WCTool` directory.
  5. Click **OK** and restart your terminal.

Once added, you can use the `ccwc` command from anywhere in the terminal.

---

## **Usage**
### **Command Syntax**
```
ccwc [command] [file_path]
```
- `[command]` - The operation you want to perform (see **Valid Commands** below).
- `[file_path]` - The path to the text file.

### **Valid Commands**
| Command  | Description |
|----------|------------|
| `-c`     | Count the number of **bytes** in the file. |
| `-l`     | Count the number of **lines** in the file. |
| `-w`     | Count the number of **words** in the file. |
| `-m`     | Count the number of **characters** in the file. |
| `-help`  | Display the help menu with available commands. |

### **Expected Input Format**
The input should follow this format:
```
ccwc -w sample.txt
```
This will output the word count of `sample.txt`.

---

## **Future Enhancements**
- **Support for Additional File Types**  
  - Extend compatibility beyond `.txt` files.
- **More Commands**  
  - Potentially include options for filtering output or displaying more statistics.

---

## **Contributing**
If you want to contribute to this project, feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
