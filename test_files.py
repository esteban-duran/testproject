import pytest
import json, files

@pytest.fixture
def client(request):
    client = files.app.test_client()
    return client


@pytest.mark.order1
def test_create(client):
  
        testFile3 = {'filename': 'testFile3', 'content': 'This is a test file'}
        testFile4 = {'filename': 'testFile4', 'content': 'This is a test file'}
        testFile5 = {'filename': 'testFile5', 'content': 'This is a test file'}

        execute3 = client.post('/files', data = json.dumps(testFile3), content_type='application/json')
        execute4 = client.post('/files', data = json.dumps(testFile4), content_type='application/json')
        execute5 = client.post('/files', data = json.dumps(testFile5), content_type='application/json')

        assert execute3.status == '201 CREATED'
        assert execute4.status == '201 CREATED'
        assert execute5.status == '201 CREATED'

        #assert get_content("testFile3") == "This is a test file"
        #assert get_content("testFile4") == "This is a test file"
        #assert get_content("testFile5") == "This is a test file"


@pytest.mark.order2
def test_recent_file(client):

        execute1 = client.get('/files/recently_created',follow_redirects=True)

        assert "testFile3" in execute1.data
        assert "testFile4" in execute1.data
        assert "testFile5" in execute1.data

@pytest.mark.order3
def test_get_all_files(client):

        execute1 = client.get('/files',follow_redirects=True)

        assert "testFile3" in execute1.data
        assert "testFile4" in execute1.data
        assert "testFile5" in execute1.data

@pytest.mark.order4
def test_remove_files(client):

        client.delete('/files', follow_redirects=True)

        execute1 = client.get('/files',follow_redirects=True)

        assert "testFile3" not in execute1.data
        assert "testFile4" not in execute1.data
        assert "testFile5" not in execute1.data
