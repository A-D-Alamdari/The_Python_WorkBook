"""
Exercise 159: RepeatedWords

    Spelling mistakes are only one of many different kinds of errors that might appear in
    a writtenwork. Another error that is common for some writers is a repeatedword. For
    example, an author might inadvertently duplicate a word, as shown in the following
    sentence:

                At least one value must be entered
                entered in order to compute the average.

    Some word processors will detect this error and identify it when a spelling or grammar
    check is performed.
    In this exercise you will write a program that detects repeated words in a text file.
    When a repeated word is found your program should display a message that contains
    the line number and the repeated word. Ensure that your program correctly handles
    the case where the same word appears at the end of one line and the beginning of the
    following line, as shown in the previous example. The name of the file to examine will
    be provided as the program’s only command line parameter. Display an appropriate
    error message if the user fails to provide a command line parameter, or if an error
    occurs while processing the file.
"""