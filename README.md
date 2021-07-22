
From JMV/Java run Python code that is using packages like `requests`,
using GraalVM with Python module (`graalpython`).


- No java dependencies, only Java code example and maven pom.xml example to handle Python setup.
- Specify Python direct requierements in `req.txt`
- Ready for production! Python code can be bundled into .jar or be external.
 Python packages can be bundled into .jar, but GraalVM cannot yet execute this way, 
 so they must be external to .jar file.

This template is based on https://github.com/hpi-swa-lab/graalpython-java-example

# Quick start

1. Download [GraalVM](https://www.graalvm.org/downloads/) and set your `JAVA_HOME` to point to it.  
Make sure you have installed Python support:
```
"${JAVA_HOME}"/bin/gu install python
```

2. Compile the example:
```
mvn package
```

3. Run the example:
```
mvn exec:exec
```
or
```
java -jar target/graalpython-java-1.0.jar
```

See output like

```
Hello Java!
11.0.11
11.0.11+8-jvmci-21.1-b05
venv/bin/graalpython
Hello Python!  <-- from this point it is from python
3.8.5 (Fri Jun 25 17:55:09 CST 2021)
[Graal, GraalVM CE, Java 11.0.11]
{'data': {'indexingStatusForCurrentVersion': None}}  <-- json from python requests
```

# To use

    git clone https://github.com/paulvi/graalpython-java-template
    mvn generate-resources

# Deploy to production

Build:

    mvn package

Distribute:  
copy target/your.jar, pom.xml, req.txt to some new location   

    mkdir dist
    cp ./{target/*.jar,pom.xml,req.txt} dist/

Run:

    cd dist
    mvn generate-resources
    java -jar graalpython-java.jar


# To recreate

This project is created as Python project (using `graalpython`),
then converted into Java project by adding maven pom.xml.

Create new graalpython project:

    mkdir dirname && cd dirname
    graalpython -m venv venv
    source venv/bin/activate

To see list of supported packages:

    graalpython -m ginstall install --help

Install `requests`

    graalpython -m ginstall install requests

Document dependencies

    pip freeze > req.txt

Run (using `graalpython` actually):

    python health.py

At this point this is still Python project. 
You can to open with PyCharn, however PyCharn does not support (yet) running `.py` files, 
even though `venv\bin\python` is commonly used.
To have this project as Java add maven pom.xml, `src/main/java` Java sources.
How you can open in IDEA, Eclipse as maven project.

Converting into Java maven project:

    cp pomx.xml, src/

Docs
- https://www.graalvm.org/python/
- https://www.graalvm.org/reference-manual/python/
- https://www.graalvm.org/reference-manual/python/Packages/
