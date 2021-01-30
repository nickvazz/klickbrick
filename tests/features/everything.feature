Feature: Says hello

    Scenario:   Klickbrick says hello
        Given   installed klickbrick
        When    using klickbrick hello
        Then    says "Hello World"

    Scenario:   Klickbrick says hello to name
        Given   installed klickbrick
        When    using klickbrick hello with a name
        Then    says "Hello [NAME]"
