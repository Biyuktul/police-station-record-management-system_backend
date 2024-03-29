from rest_framework import serializers
from .models import officer, Privileges, Evidences, Victims, Suspect, Cases, Witness, Team, FIR, Complaints, Civilian, Report, Post, Department


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = officer
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privileges
        fields = '__all__'


class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidences
        fields = '__all__'


class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victims
        fields = '__all__'


class SuspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suspect
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = '__all__'


class WitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Witness
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class FIRSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIR
        fields = '__all__'


class ComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaints
        fields = '__all__'


class CivilianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civilian
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
