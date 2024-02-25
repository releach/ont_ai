# ttl_ontology.py

ontology_data = '''
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix dc11: <http://purl.org/dc/elements/1.1/> .
@prefix wot: <http://xmlns.com/wot/0.1/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ns0: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix schema: <http://schema.org/> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

foaf:
  a owl:Ontology ;
  dc11:title "Friend of a Friend (FOAF) vocabulary" ;
  dc11:description "The Friend of a Friend (FOAF) RDF vocabulary, described using W3C RDF Schema and the Web Ontology Language." .

wot:assurance a owl:AnnotationProperty .
wot:src_assurance a owl:AnnotationProperty .
<http://www.w3.org/2003/06/sw-vocab-status/ns#term_status> a owl:AnnotationProperty .
dc11:description a owl:AnnotationProperty .
dc11:title a owl:AnnotationProperty .
dc11:date a owl:AnnotationProperty .
rdfs:Class a owl:Class .
foaf:LabelProperty
  a rdfs:Class, owl:Class ;
  ns0:term_status "unstable" ;
  rdfs:label "Label Property" ;
  rdfs:comment "A foaf:LabelProperty is any RDF property with texual values that serve as labels." ;
  rdfs:isDefinedBy foaf: .

foaf:Person
  a rdfs:Class, owl:Class ;
  rdfs:label "Person" ;
  rdfs:comment "A person." ;
  ns0:term_status "stable" ;
  owl:equivalentClass schema:Person, <http://www.w3.org/2000/10/swap/pim/contact#Person> ;
  rdfs:subClassOf foaf:Agent, geo:SpatialThing ;
  rdfs:isDefinedBy foaf: ;
  owl:disjointWith foaf:Organization, foaf:Project .

foaf:Agent
  a owl:Class, rdfs:Class ;
  ns0:term_status "stable" ;
  rdfs:label "Agent" ;
  rdfs:comment "An agent (eg. person, group, software or physical artifact)." ;
  owl:equivalentClass dc:Agent .

geo:SpatialThing
  a owl:Class ;
  rdfs:label "Spatial Thing" .

foaf:Document
  a rdfs:Class, owl:Class ;
  rdfs:label "Document" ;
  rdfs:comment "A document." ;
  ns0:term_status "stable" ;
  owl:equivalentClass schema:CreativeWork ;
  rdfs:isDefinedBy foaf: ;
  owl:disjointWith foaf:Organization, foaf:Project .

foaf:Organization
  a rdfs:Class, owl:Class ;
  rdfs:label "Organization" ;
  rdfs:comment "An organization." ;
  ns0:term_status "stable" ;
  rdfs:subClassOf foaf:Agent ;
  rdfs:isDefinedBy foaf: ;
  owl:disjointWith foaf:Person, foaf:Document .

foaf:Group
  a rdfs:Class, owl:Class ;
  ns0:term_status "stable" ;
  rdfs:label "Group" ;
  rdfs:comment "A class of Agents." ;
  rdfs:subClassOf foaf:Agent .

foaf:Project
  a rdfs:Class, owl:Class ;
  ns0:term_status "testing" ;
  rdfs:label "Project" ;
  rdfs:comment "A project (a collective endeavour of some kind)." ;
  rdfs:isDefinedBy foaf: ;
  owl:disjointWith foaf:Person, foaf:Document .

foaf:Image
  a rdfs:Class, owl:Class ;
  ns0:term_status "stable" ;
  rdfs:label "Image" ;
  rdfs:comment "An image." ;
  owl:equivalentClass schema:ImageObject ;
  rdfs:subClassOf foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:PersonalProfileDocument
  a rdfs:Class, owl:Class ;
  rdfs:label "PersonalProfileDocument" ;
  rdfs:comment "A personal profile RDF document." ;
  ns0:term_status "testing" ;
  rdfs:subClassOf foaf:Document .

foaf:OnlineAccount
  a rdfs:Class, owl:Class ;
  ns0:term_status "testing" ;
  rdfs:label "Online Account" ;
  rdfs:comment "An online account." ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subClassOf owl:Thing .

owl:Thing rdfs:label "Thing" .
foaf:OnlineGamingAccount
  a rdfs:Class, owl:Class ;
  ns0:term_status "unstable" ;
  rdfs:label "Online Gaming Account" ;
  rdfs:comment "An online gaming account." ;
  rdfs:subClassOf foaf:OnlineAccount ;
  rdfs:isDefinedBy foaf: .

foaf:OnlineEcommerceAccount
  a rdfs:Class, owl:Class ;
  ns0:term_status "unstable" ;
  rdfs:label "Online E-commerce Account" ;
  rdfs:comment "An online e-commerce account." ;
  rdfs:subClassOf foaf:OnlineAccount ;
  rdfs:isDefinedBy foaf: .

foaf:OnlineChatAccount
  a rdfs:Class, owl:Class ;
  ns0:term_status "unstable" ;
  rdfs:label "Online Chat Account" ;
  rdfs:comment "An online chat account." ;
  rdfs:subClassOf foaf:OnlineAccount ;
  rdfs:isDefinedBy foaf: .

foaf:mbox
  a rdf:Property, owl:InverseFunctionalProperty, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "personal mailbox" ;
  rdfs:comment "A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox." ;
  rdfs:domain foaf:Agent ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:mbox_sha1sum
  a rdf:Property, owl:InverseFunctionalProperty, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "sha1sum of a personal mailbox URI name" ;
  rdfs:comment "The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox." ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:gender
  a rdf:Property, owl:FunctionalProperty, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "gender" ;
  rdfs:comment "The gender of this Agent (typically but not necessarily 'male' or 'female')." ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:geekcode
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "geekcode" ;
  rdfs:comment "A textual geekcode for this person, see http://www.geekcode.com/geek.html" ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:dnaChecksum
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "DNA checksum" ;
  rdfs:comment "A checksum for the DNA of some thing. Joke." ;
  rdfs:isDefinedBy foaf: ;
  rdfs:range rdfs:Literal .

foaf:sha1
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "unstable" ;
  rdfs:label "sha1sum (hex)" ;
  rdfs:comment "A sha1sum hash, in hex." ;
  rdfs:domain foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:based_near
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "based near" ;
  rdfs:comment "A location that something is based near, for some broadly human notion of near." ;
  rdfs:domain geo:SpatialThing ;
  rdfs:range geo:SpatialThing ;
  rdfs:isDefinedBy foaf: .

foaf:title
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "title" ;
  rdfs:comment "Title (Mr, Mrs, Ms, Dr. etc)" ;
  rdfs:isDefinedBy foaf: .

foaf:nick
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "nickname" ;
  rdfs:comment "A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames)." ;
  rdfs:isDefinedBy foaf: .

foaf:jabberID
  a rdf:Property, owl:DatatypeProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "jabber ID" ;
  rdfs:comment "A jabber ID for something." ;
  rdfs:isDefinedBy foaf: ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal .

foaf:aimChatID
  a rdf:Property, owl:DatatypeProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "AIM chat ID" ;
  rdfs:comment "An AIM chat ID" ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subPropertyOf foaf:nick ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal .

foaf:skypeID
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "Skype ID" ;
  rdfs:comment "A Skype ID" ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subPropertyOf foaf:nick ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal .

foaf:icqChatID
  a rdf:Property, owl:DatatypeProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "ICQ chat ID" ;
  rdfs:comment "An ICQ chat ID" ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subPropertyOf foaf:nick ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal .

foaf:yahooChatID
  a rdf:Property, owl:DatatypeProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "Yahoo chat ID" ;
  rdfs:comment "A Yahoo chat ID" ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subPropertyOf foaf:nick ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal .

foaf:msnChatID
  a rdf:Property, owl:DatatypeProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "MSN chat ID" ;
  rdfs:comment "An MSN chat ID" ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subPropertyOf foaf:nick ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal .

foaf:name
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "name" ;
  rdfs:comment "A name for some thing." ;
  rdfs:domain owl:Thing ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: ;
  rdfs:subPropertyOf rdfs:label .

foaf:firstName
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "firstName" ;
  rdfs:comment "The first name of a person." ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:lastName
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "lastName" ;
  rdfs:comment "The last name of a person." ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:givenName
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "Given name" ;
  rdfs:comment "The given name of some person." ;
  rdfs:isDefinedBy foaf: .

foaf:givenname
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "Given name" ;
  rdfs:comment "The given name of some person." ;
  rdfs:isDefinedBy foaf: .

foaf:surname
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "Surname" ;
  rdfs:comment "The surname of some person." ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:family_name
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "family_name" ;
  rdfs:comment "The family name of some person." ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:familyName
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "familyName" ;
  rdfs:comment "The family name of some person." ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:phone
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "phone" ;
  rdfs:comment "A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel)." ;
  rdfs:isDefinedBy foaf: .

foaf:homepage
  a rdf:Property, owl:ObjectProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "stable" ;
  rdfs:label "homepage" ;
  rdfs:comment "A homepage for some thing." ;
  rdfs:subPropertyOf foaf:page, foaf:isPrimaryTopicOf ;
  rdfs:domain owl:Thing ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:weblog
  a rdf:Property, owl:ObjectProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "stable" ;
  rdfs:label "weblog" ;
  rdfs:comment "A weblog of some thing (whether person, group, company etc.)." ;
  rdfs:subPropertyOf foaf:page ;
  rdfs:domain foaf:Agent ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:openid
  a rdf:Property, owl:ObjectProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "openid" ;
  rdfs:comment "An OpenID for an Agent." ;
  rdfs:subPropertyOf foaf:isPrimaryTopicOf ;
  rdfs:domain foaf:Agent ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:tipjar
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "tipjar" ;
  rdfs:comment "A tipjar document for this agent, describing means for payment and reward." ;
  rdfs:subPropertyOf foaf:page ;
  rdfs:domain foaf:Agent ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:plan
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "plan" ;
  rdfs:comment "A .plan comment, in the tradition of finger and '.plan' files." ;
  rdfs:isDefinedBy foaf: ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal .

foaf:made
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "made" ;
  rdfs:comment "Something that was made by this agent." ;
  rdfs:domain foaf:Agent ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: ;
  owl:inverseOf foaf:maker .

foaf:maker
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "maker" ;
  rdfs:comment "An agent that  made this thing." ;
  owl:equivalentProperty dc:creator ;
  rdfs:domain owl:Thing ;
  rdfs:range foaf:Agent ;
  rdfs:isDefinedBy foaf: ;
  owl:inverseOf foaf:made .

foaf:img
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "image" ;
  rdfs:comment "An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)." ;
  rdfs:domain foaf:Person ;
  rdfs:range foaf:Image ;
  rdfs:subPropertyOf foaf:depiction ;
  rdfs:isDefinedBy foaf: .

foaf:depiction
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "depiction" ;
  rdfs:comment "A depiction of some thing." ;
  rdfs:domain owl:Thing ;
  rdfs:range foaf:Image ;
  rdfs:isDefinedBy foaf: ;
  owl:inverseOf foaf:depicts .

foaf:depicts
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "depicts" ;
  rdfs:comment "A thing depicted in this representation." ;
  rdfs:range owl:Thing ;
  rdfs:domain foaf:Image ;
  rdfs:isDefinedBy foaf: ;
  owl:inverseOf foaf:depiction .

foaf:thumbnail
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "thumbnail" ;
  rdfs:comment "A derived thumbnail image." ;
  rdfs:domain foaf:Image ;
  rdfs:range foaf:Image ;
  rdfs:isDefinedBy foaf: .

foaf:myersBriggs
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "myersBriggs" ;
  rdfs:comment "A Myers Briggs (MBTI) personality classification." ;
  rdfs:domain foaf:Person ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:workplaceHomepage
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "workplace homepage" ;
  rdfs:comment "A workplace homepage of some person; the homepage of an organization they work for." ;
  rdfs:domain foaf:Person ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:workInfoHomepage
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "work info homepage" ;
  rdfs:comment "A work info homepage of some person; a page about their work for some organization." ;
  rdfs:domain foaf:Person ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:schoolHomepage
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "schoolHomepage" ;
  rdfs:comment "A homepage of a school attended by the person." ;
  rdfs:domain foaf:Person ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:knows
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "knows" ;
  rdfs:comment "A person known by this person (indicating some level of reciprocated interaction between the parties)." ;
  rdfs:domain foaf:Person ;
  rdfs:range foaf:Person ;
  rdfs:isDefinedBy foaf: .

foaf:interest
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "interest" ;
  rdfs:comment "A page about a topic of interest to this person." ;
  rdfs:domain foaf:Agent ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:topic_interest
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "topic_interest" ;
  rdfs:comment "A thing of interest to this person." ;
  rdfs:domain foaf:Agent ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:publications
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "publications" ;
  rdfs:comment "A link to the publications of this person." ;
  rdfs:domain foaf:Person ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:currentProject
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "current project" ;
  rdfs:comment "A current project this person works on." ;
  rdfs:domain foaf:Person ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:pastProject
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "past project" ;
  rdfs:comment "A project this person has previously worked on." ;
  rdfs:domain foaf:Person ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:fundedBy
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "funded by" ;
  rdfs:comment "An organization funding a project or person." ;
  rdfs:domain owl:Thing ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:logo
  a rdf:Property, owl:ObjectProperty, owl:InverseFunctionalProperty ;
  ns0:term_status "testing" ;
  rdfs:label "logo" ;
  rdfs:comment "A logo representing some thing." ;
  rdfs:domain owl:Thing ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:topic
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "topic" ;
  rdfs:comment "A topic of some page or document." ;
  rdfs:domain foaf:Document ;
  rdfs:range owl:Thing ;
  owl:inverseOf foaf:page ;
  rdfs:isDefinedBy foaf: .

foaf:primaryTopic
  a rdf:Property, owl:FunctionalProperty, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "primary topic" ;
  rdfs:comment "The primary topic of some page or document." ;
  rdfs:domain foaf:Document ;
  rdfs:range owl:Thing ;
  owl:inverseOf foaf:isPrimaryTopicOf ;
  rdfs:isDefinedBy foaf: .

foaf:focus
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "focus" ;
  rdfs:comment "The underlying or 'focal' entity associated with some SKOS-described concept." ;
  rdfs:domain skos:Concept ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

skos:Concept rdfs:label "Concept" .
foaf:isPrimaryTopicOf
  a rdf:Property, owl:InverseFunctionalProperty ;
  ns0:term_status "stable" ;
  rdfs:label "is primary topic of" ;
  rdfs:comment "A document that this thing is the primary topic of." ;
  rdfs:subPropertyOf foaf:page ;
  owl:inverseOf foaf:primaryTopic ;
  rdfs:domain owl:Thing ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:page
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "page" ;
  rdfs:comment "A page or document about this thing." ;
  rdfs:domain owl:Thing ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: ;
  owl:inverseOf foaf:topic .

foaf:theme
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "theme" ;
  rdfs:comment "A theme." ;
  rdfs:domain owl:Thing ;
  rdfs:range owl:Thing ;
  rdfs:isDefinedBy foaf: .

foaf:account
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "account" ;
  rdfs:comment "Indicates an account held by this agent." ;
  rdfs:domain foaf:Agent ;
  rdfs:range foaf:OnlineAccount ;
  rdfs:isDefinedBy foaf: .

foaf:holdsAccount
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "archaic" ;
  rdfs:label "account" ;
  rdfs:comment "Indicates an account held by this agent." ;
  rdfs:domain foaf:Agent ;
  rdfs:range foaf:OnlineAccount ;
  rdfs:isDefinedBy foaf: .

foaf:accountServiceHomepage
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "testing" ;
  rdfs:label "account service homepage" ;
  rdfs:comment "Indicates a homepage of the service provide for this online account." ;
  rdfs:domain foaf:OnlineAccount ;
  rdfs:range foaf:Document ;
  rdfs:isDefinedBy foaf: .

foaf:accountName
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "testing" ;
  rdfs:label "account name" ;
  rdfs:comment "Indicates the name (identifier) associated with this online account." ;
  rdfs:domain foaf:OnlineAccount ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:member
  a rdf:Property, owl:ObjectProperty ;
  ns0:term_status "stable" ;
  rdfs:label "member" ;
  rdfs:comment "Indicates a member of a Group" ;
  rdfs:domain foaf:Group ;
  rdfs:range foaf:Agent ;
  rdfs:isDefinedBy foaf: .

foaf:membershipClass
  a rdf:Property, owl:AnnotationProperty ;
  ns0:term_status "unstable" ;
  rdfs:label "membershipClass" ;
  rdfs:comment "Indicates the class of individuals that are a member of a Group" ;
  rdfs:isDefinedBy foaf: .

foaf:birthday
  a rdf:Property, owl:FunctionalProperty, owl:DatatypeProperty ;
  ns0:term_status "unstable" ;
  rdfs:label "birthday" ;
  rdfs:comment "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:age
  a rdf:Property, owl:FunctionalProperty, owl:DatatypeProperty ;
  ns0:term_status "unstable" ;
  rdfs:label "age" ;
  rdfs:comment "The age in years of some agent." ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .

foaf:status
  a rdf:Property, owl:DatatypeProperty ;
  ns0:term_status "unstable" ;
  rdfs:label "status" ;
  rdfs:comment "A string expressing what the user is happy for the general public (normally) to know about their current activity." ;
  rdfs:domain foaf:Agent ;
  rdfs:range rdfs:Literal ;
  rdfs:isDefinedBy foaf: .
  '''
