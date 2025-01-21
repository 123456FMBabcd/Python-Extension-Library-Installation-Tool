##Python-Extension-Library-Installation-Tool

**一、项目简介**
这是一个个人开发的项目，旨在帮助 Python 初学者更方便地安装、卸载扩展库。它提供了一个简单易用的图形用户界面（GUI），用户可以轻松管理 Python 扩展库，同时支持使用中国的各大优秀镜像源，以解决在使用官方源时可能出现的网络速度慢等问题。

**二、功能特性**
1. **扩展库安装与卸载**：
    - 在输入框中输入要安装或卸载的 Python 扩展库的名称，点击相应按钮，程序自动调用 `pip` 命令进行操作。
    - 可以选择不同的镜像源，如清华镜像、阿里镜像、中科大镜像、豆瓣镜像等，以加快下载或卸载速度。
    - 安装或卸载操作完成后，会通过弹窗显示相应的成功或失败信息。
2. **查看已安装的扩展库**：
    - 点击“查看已安装”按钮，会弹出一个新窗口，显示当前 Python 环境中已安装的扩展库列表。
    - 列表使用 `Listbox` 展示，并带有滚动条，方便用户查看。
3. **打开扩展库的安装位置**：
    - 输入扩展库名称，点击相应操作，可打开该扩展库在本地的安装位置。若出现错误，会显示错误信息。
4. **恢复默认设置**：
    - 可以将镜像源设置恢复到默认的 `pypi.org`。
5. **配置保存**：
    - 程序会将用户选择的镜像源信息保存到 `config.json` 文件中，下次打开程序时自动加载。

**三、使用方法**
1. **启动程序**：
    - 运行 `Python Extension Library Installation Tool V1.0.0.exe`（可在 `nuitka.dist` 或 `pyinstaller.dist` 文件夹中找到），根据自己的操作系统选择对应的版本（目前仅支持 Windows 11 64 位，其他版本未验证）。
2. **安装扩展库**：
    - 在输入框中输入要安装的扩展库名称。
    - 从“安装源”下拉列表中选择所需的镜像源（可选）。
    - 点击“安装”按钮，等待安装完成并查看结果弹窗。
3. **卸载扩展库**：
    - 在输入框中输入要卸载的扩展库名称。
    - 点击“卸载”按钮，等待卸载完成并查看结果弹窗。
4. **查看已安装的扩展库**：
    - 点击“查看已安装”按钮，在弹出的新窗口中查看已安装的扩展库列表。
5. **打开扩展库的安装位置**：
    - 在输入框中输入扩展库名称，点击相应操作打开其安装位置。
6. **恢复默认设置**：
    - 点击“恢复默认设置”按钮，将镜像源恢复为 `pypi.org`。

**四、注意事项**
1. 仅提供中文版本软件，对于中国的 Python 初学者用户更为友好。
2. 程序使用 `tkinter`、`subprocess`、`easygui` 等 Python 库，这些库通常会随 Python 安装一起提供，但 `easygui` 可能需要额外安装，可使用 `pip install easygui` 进行安装。
3. 目前暂不提供 32 位 Windows 版本，仅支持 Windows 11 64 位，使用其他版本的用户请谨慎使用并自行测试兼容性。


**五、更新日志**
- 2025-01-21 更新：上传第一版，包括功能：下载、卸载库，查看已有库，选择镜像源。
- 2025-01-21 计划：添加亮暗两种风格供用户选择。


**六、联系我们**
若在使用过程中遇到问题或有任何建议，请联系2198789746@qq.com或fatheriscoming@126.com  



   
##Python-Extension-Library-Installation-Tool

**I. Project Introduction**
This is a project developed by an individual, aiming to help Python beginners install and uninstall extension libraries more conveniently. It provides a simple and easy-to-use Graphical User Interface (GUI) that allows users to manage Python extension libraries easily. It also supports various excellent mirror sources in China, which helps solve the problem of slow network speed when using the official source.

**II. Features**
1. **Extension Library Installation and Uninstallation**:
    - Enter the name of the Python extension library to be installed or uninstalled in the input box, and click the corresponding button to perform operations via the `pip` command.
    - You can select different mirror sources, such as Tsinghua mirror, Ali mirror, USTC mirror, Douban mirror, etc., to speed up the download or uninstallation.
    - After the installation or uninstallation operation is completed, a corresponding success or failure message will be displayed through a pop-up window.
2. **View Installed Extension Libraries**:
    - Click the "View Installed" button, and a new window will pop up, showing the list of installed extension libraries in the current Python environment.
    - The list is displayed using a `Listbox` with a scrollbar for easy viewing.
3. **Open the Installation Location of Extension Libraries**:
    - Enter the name of the extension library and click the corresponding operation to open its local installation location. If an error occurs, an error message will be displayed.
4. **Restore Default Settings**:
    - You can restore the mirror source setting to the default `pypi.org`.
5. **Configuration Saving**:
    - The program will save the user's selected mirror source information in the `config.json` file and load it automatically when the program is opened next time.

**III. Usage**
1. **Launch the Program**:
    - Run `Python Extension Library Installation Tool V1.0.0.exe` (can be found in the `nuitka.dist` or `pyinstaller.dist` folder), and select the corresponding version according to your operating system (currently only supports Windows 11 64-bit, other versions have not been verified).
2. **Install Extension Libraries**:
    - Enter the name of the extension library to be installed in the input box.
    - Select the desired mirror source from the "Installation Source" drop-down list (optional).
    - Click the "Install" button, wait for the installation to complete, and check the result pop-up window.
3. **Uninstall Extension Libraries**:
    - Enter the name of the extension library to be uninstalled in the input box.
    - Click the "Uninstall" button, wait for the uninstallation to complete, and check the result pop-up window.
4. **View Installed Extension Libraries**:
    - Click the "View Installed" button to view the list of installed extension libraries in the popped-up new window.
5. **Open the Installation Location of Extension Libraries**:
    - Enter the name of the extension library in the input box and click the corresponding operation to open its installation location.
6. **Restore Default Settings**:
    - Click the "Restore Default Settings" button to restore the mirror source to `pypi.org`.

**IV. Precautions**
1. Only the Chinese version of the software is provided, which is more user-friendly for Chinese Python beginners.
2. The program uses Python libraries such as `tkinter`, `subprocess`, and `easygui`. These libraries are usually provided with Python installation, but `easygui` may need to be installed separately. You can use `pip install easygui` for installation.
3. The 32-bit Windows version is not provided at present, and only Windows 11 64-bit is supported. Users of other versions should use it with caution and test compatibility by themselves.


**V. Update Log**
- 2025-01-21 Update: The first version was uploaded, including functions: downloading libraries, uninstalling libraries, viewing existing libraries, and selecting mirror sources.
- 2025-01-21 Plan: Add two styles, light and dark, for users to choose from.


**VI. Contact Us**
If you encounter any problems or have any suggestions during use, please contact 2198789746@qq.com or fatheriscoming@126.com.

