import { Grid, makeStyles, Container, Typography } from "@material-ui/core";
import {
  TextField,
  Button,
} from "@material-ui/core";
const useStyles = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(3),
  },
}));

function Home() {
  const classes = useStyles();

  return (
    <Container maxWidth="sm" className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <TextField
            fullWidth={true}
            label="id пользователя"
            variant="filled"
          />
          <Button
              variant="contained"
              color="primary"
              type="submit"
            >
              Найти пользователя
            </Button>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Home;
