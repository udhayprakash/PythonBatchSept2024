# PythonBatchSept2024

## Git Commands

### To clone a repository, 
    git clone https URL 

### To stage the changes
    git add <filename>

### To commit the changes
    git commit -m "commit message"

### To push the changes,
    git push origin <sourceBRanch>

        class01 -> main
        git push origin class01

### To check/verify the  modified content in existing file,
    git diff <filename>

## Daily 
    To check the branch is clean, 

        git status 

    To checkout to the main branch 
        git checkout main 

    To get the latest changes 
        git pull origin main 

    To create new branch 
        git checkout -b <NEW BRANCH NAME>

## Course Completed 

[class01 sept 18th](https://us06web.zoom.us/rec/share/FmBPyvAsTuu_uEcE6glhkCmt-_uc9Uc7BxEqTUUSk021nt-WvW1inuw2CUGbkIgd.o1G7sr94PTh4lGhI)

    00. Dev Setup
        Installing IDE/Editor
        Installing Python and local setup
        Github access, creating project
    

[class02 sept 19th](https://us06web.zoom.us/rec/share/ixzGLoV-AOYOk-7c9mWF8pvZiTMI1pu1HmN9N3XWzcnYXUqDsYtAXtb_z6Mw0Mvp.lwiOwyjkRBKYQ3FP) 
    
    01.Introduction

        Introduction to python
        shebang line & usage
        Dynamic Typing
        Basic data types supports 
        Indentation issue 

    
[class03 sept 23rd](https://us06web.zoom.us/rec/share/Ojz7TIC5eHWjtgZUliMt1Ng2lbDXE-XWPHTQFNncXe24fdmUkHU0Un9otmq4tLQ.SU3lKLBmttvQAPkW)
        built-in functions
        Comment Operator
        keywords and Identifiers
        strictly-typed and data type conversions
        python interactive mode
        Line continuation operator
    

[class 04 sept 24th](https://us06web.zoom.us/rec/share/3uKuzn4vMrVTMJZTO2TF51rY_25y3zx-hoo0BT6mZajgGpXHvCEmtJ15j4ZsCsDO.UshItZWejOCSGHwD)

    02.Basics
        Arithmetic operations
            +, -, , /, //, %, *
            divmod() function
            compound operations
            jupyter notebook 

[class 05 sept 25th](https://us06web.zoom.us/rec/share/sBTQ8chSIAhLL70reNwW1Wwx4_CpAGfQ8DGiE8LXHnVtStQBb82toZQ_ZwKHIaUN.LlncP18GxVCU3Fca)
       
            Practical Problem solving
            working with complex numbers
            abs() function
            Operator precedence in Arithmetic operations

[class 06 sept 26th]()

    02.Basics
        String operations
            Usage of single, double and triple quotes
            len() function
            Indexing 
            
            
[class 07 sept 30th]()
          
            Slicing Strings
            string attributes
            String formatting: old & new styles, f-strings
            bytearray() and byte() strings
            unicode strings
        Usage of help
        Usage of pydoc

    03.Language Components
        Relational Operations
        Logical Operations
        Boolean Operations
        Bitwise Operations
        Identity Operations
        range() function
        Conditional Operations
        Structural Pattern Matching
        Loops: for & while, break, continue, pass, sys.exit
        Walrus Operator

    04.Exception Handling
        Exceptions Hierarchy
        Different types of errors, error vs exception and exception groups
        Handling single and multiple exceptions
        raising exceptions
        asserts
        traceback
        warnings

    05.Debugging
        Importance of logical errors
        Debugging with pydevd
        Debugging with pdb, ipdb, pudb
        breakpoint() function
        PYTHONBREAKPOINT environment variable usage

    06.Collections
        Lists
        Tuples & namedtuples
        Sets
        Dictionaries
            zip() function
            workaround for switch case
        Comprehensions
        Working with Iterables - sum(), max(), min()

    07.Functions
        Functions with & without arguments, keyword arguments
        Functions with Different return types and unpacking
        Functions with with Default arguments
        variadic functions : variable arguments and variable keyword arguments
        Functions with keyword only arguments
        Scoping: Global vs Local
            call by reference
            call by value
        Partial Functions
        Anonymous(Lambda) Functions
        Higher order functions: map(), filter(), functool.reduce()
        Recursions and recursions limit
        inner functions
        closures

    08.Decorator Design Pattern
        Necessity
        function Decorator
        Practical Examples
        syntactic sugar for decorators
        multiple decorators on same function
        decorators with arguments
        functools - wrap, lru_cache
        class decorator

    09.Iterables, Iterators, Generators and co-routines
        Iterables
            different ways of extracting values from iterables
        Iterators
            iter() protocol
            itertools module
        Generators
            yield vs return
            function vs Generator
            Generator pipelining
            Generator Expression
        Coroutine
            Generator vs Coroutine
            coroutine pipelining

    10.Modules
        Basic Modules
            - math, sys, argparse, os, shutil, pathlib, subprocess, getpass
        time related
            - time, datetime, pytz, timeit, calendar
        concurrency
            - Multiprocessing, Multithreading
        others
            - random, collections, atexit, contextlib, base64, turtle, tqdm

        create user-defined module
        creating user-defined package

    11.File Operations
        flat files
        Non-flat files
            pickle
            shelve
            xml
            csv
            dat
            xls/xlsx
            json
            yaml
            parquet
            avro
        Image files
            displaying, creating and editing images
        zipping files: .zip, .tar
        pdf files
        config files : .ini, .cfg
        pyw files

    12.Logging
        Simple logging
        configuring log file
        formatting logs and adding timestamp
        working with file handler and stream hanlder
        configuring multiple handlers
        color logging
        Rotating logger

    13. OOP
        Importance of OOP
        Instantiation and managing attributes
        constructor and Importance of self
        instance and class variables
        Encapsulation
        MRO, Single and multiple inheritance, composition
        Method Overwriting, Operator Overloading
        instance, class and static methods
        property decorator
        Dunder(magic) methods
        reprlib module
        creating context manager class
        Dataclasses
        Abstract Classes

    14. Code Quality
        typing
        Doctest
        unittest

    15. Regular Expressions
        re module
        compiling regex objects
        match & search
        find & finditer
        regex Flags
        Greedy & Non-Greedy patterns
        findall & finditer
        sub and subn
        regex Flags
        groups and groupdicts
        Pearl-style regexes
        Realworld Problem (log analyses, email Validation, etc)

    16. Databases
        db files - sqlite3
        Relational DB - MySQL
        Non-Relational DB - mongoDB

    17. Web Services
        consuming REST API
        scraping web pages
        urllib, requests

    18. Data Science
        statistics
        Numpy
        Pandas
        Matplotlib
