#!/usr/bin/env python
"""
Copyright 2012 GroupDocs.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class JobInputDocument:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'status': 'str',
            'output_formats': 'str',
            'type_str': 'str',
            'access': 'str',
            'type': 'str',
            'url': 'str',
            'file_type': 'str',
            'version': 'int',
            'size': 'long',
            'guid': 'str',
            'id': 'float',
            'document_path': 'str',
            'supported_output_file_types': 'list[str]',
            'proc_date': 'long',
            'name': 'str',
            'file_type_str': 'str',
            'outputs': 'list[JobOutputDocument]',
            'actions': 'str',
            'job_errors': 'list[JobErrorInfo]'

        }


        self.status = None # str
        self.output_formats = None # str
        self.type_str = None # str
        self.access = None # str
        self.type = None # str
        self.url = None # str
        self.file_type = None # str
        self.version = None # int
        self.size = None # long
        self.guid = None # str
        self.id = None # float
        self.document_path = None # str
        self.supported_output_file_types = None # list[str]
        self.proc_date = None # long
        self.name = None # str
        self.file_type_str = None # str
        self.outputs = None # list[JobOutputDocument]
        self.actions = None # str
        self.job_errors = None # list[JobErrorInfo]
        
